# This file stores the program to data pull from reddit's API
# reddit_comments is the list with comment results


import praw
import config

reddit = praw.Reddit(
    client_id=config.client_id,
    client_secret=config.client_secret,
    user_agent=config.user_agent,
)

reddit_comments = []

for submission in reddit.subreddit('all').search(f'{config.company_query} news', limit=config.limitcomments):
    try: 
        top_level_comments = list(submission.comments)
        for comment in top_level_comments:
            reddit_comments.append(comment.body)
    except Exception as e:
        print(f"Not enough comments; error was produced")


########################################## PICKLING DATA ##############################################################
# *decided not to pickle data 

# import pickle

# with open('reddit_comments.pickle','wb') as f:
#     pickle.dump(reddit_comments, f)

# with open('reddit_comments.pickle', 'r') as f:
#     reload_copy = pickle.load(f)
# TO CALL COPY: datapull_reddit.reload_copy

