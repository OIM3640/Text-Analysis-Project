# from github instructions
import praw
import nltk
nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer
# from ChatGPT
import matplotlib.pyplot as plt
# looked up how to hide API keys in a separate file on ChatGPT
import json

with open ('keys.json', 'r') as config_file:
    config = json.load(config_file)
#Initialize PRAW with Reddit API credentials 

reddit = praw.Reddit(
    client_id = config["API_CLIENT_ID"],
    client_secret = config["API_CLIENT_SECRET"],
    user_agent = config["API_USER_AGENT"]
)
# Used example from both Github instructions and ChatGPT on how to pull from a subreddit
#SPecify subreddit I am retrieving data from
subreddit_name = "leagueoflegends"

# looked on ChatGPT on how to create dictionaries with lists as values
# each value in the list is a post-match discussion post on the league of legends subreddit
my_dict = {
    'NA vs NA': ['17c3xsl'],
    'EU vs EU': ['17c5ymn' ],
    'China vs China': ['17cyil7', '17c9eej'],
    'Korea vs Korea': ['17c7gwo', '17cag90', '17iwe0b'],
    'NA vs EU': ['17bd094', '17dotra', '17gsm21', '17i9e7l'],
    'NA vs China': ['17bgmua', '17c569b', '17m0hhj'],
    'NA vs Korea': ['17bc0ay', '17dnvxz'],
    'EU vs China': ['17j0stv', '17beoj3','17bhkyg', '17c8h69', '17dpmzu', '17gu9ma', '17iyf26'],
    'EU vs Korea': ['17bfnt4', '17d01bt', '17ehods'],
    'China vs Korea': ['17biyo3', '17iar6z', '17dqj4v', '17hl4au', '17mtyr3', '17njdso', '17o8xjy']
    
}



#basically the entire code was looked up on ChatGPT in an iterative process 
# I first looked up how to iterate on a dictionary with lists as its values to get all the comments on each post 
# I also looked up how to calculate the average compound score  
# I then initially thought about doing a scatterplot but decided to do a bar chart and looked up how to do that as well
# When I wasn't getting the correct visualizations, I looked up what could be done to get the right bars for the bar chart
# I then looked up how to create a new dictionary based off of the sentiment scores
# Finally I looked up how to set the colors when a score is negative or positive
# Here is the ChatGPT link: https://chat.openai.com/share/0f63f15b-1aee-41bb-b2d7-ee13a6ad7ccf
def comment_sentiments (posts):
    """
    Creates a dictionary of the average compound scores with the original keys (regional matchups)
    """
    avg_scores_dict = {}
    for key, value_list in my_dict.items():
        """
        creates a list of the compound scores 
        """
        compound_scores = []
        # print(f"Key: {key}")
        for post_id in value_list:
            """
            takes each post id and collects all the comments (only the body of the comment) and puts it within a list
            """
            submission = reddit.submission(id = post_id)
            submission.comments.replace_more (limit = 10)
            all_comments = submission.comments.list()
            for comment in all_comments:
                """
                Goes through each comment and runs it through a sentiment analysis function and appends the compound values into the compound score list
                """
                sentence = comment.body
                score = SentimentIntensityAnalyzer().polarity_scores(sentence)
                compound_scores.append(score['compound'])
        avg_compound_score = sum(compound_scores)/len(compound_scores)
        avg_scores_dict[key] = avg_compound_score
        print(f'Category: {key}, Average Compound Score: {avg_compound_score}')
    print(avg_compound_score)
    return avg_scores_dict

def create_bar_charts(data_dict):
    """
    Takes the average compound values calculated in the comment_sentiments function to create a bar chart
    """
    categories = list(data_dict.keys())
    scores = list(data_dict.values())
    bar_colors = ['blue' if score >=0 else 'red' for score in scores]
    plt.figure(figsize=(10,6))
    bars = plt.bar(categories, scores, color=bar_colors)
    plt.xlabel('Regional Matchups')
    plt.ylabel('Average Compound Score')
    plt.title('League of Legends Worlds Reddit Comment Sentiment Analysis')
    plt.xticks(rotation=45)
    for bar, score in zip(bars,scores):
        """
        Formatting for the bars in the bar chart
        """
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), round(score, 2), ha='center', va='bottom')
   
    plt.show()
comment_sentiments(my_dict)
avg_scores_dict = comment_sentiments(my_dict)
create_bar_charts(avg_scores_dict)

# if __name__ == "__main__":
#     main()