
import pandas as pd
import matplotlib.pyplot as plt
import pickle

with open('combined_word_counts_west.pkl', 'rb') as f:
    combined_word_counts_west = pickle.load(f)
with open('combined_word_counts_palestine.pkl', 'rb') as f:
    combined_word_counts_palestine = pickle.load(f)

# uses pickled data from file news_parser




def visualize_most_used_words(word_dictionary, top_n=10, title=''):
    """
    This function visualizes the top words from the given dictionary and creates a top 20 histogram of them.
    """
    df = pd.DataFrame(list(word_dictionary.items()), columns=['Word', 'Count'])
    df_sorted = df.sort_values(by='Count', ascending=False)
    df_top = df_sorted.head(top_n)

    plt.figure(figsize=(10, 5))
    plt.bar(df_top['Word'], df_top['Count'], color='maroon')
    plt.xlabel('Words')
    plt.ylabel('Count')
    plt.title(f'Top {top_n} Most Used Words in {title}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Visualize the data for both dictionaries


# removes the empty character
combined_word_counts_west.pop('', None)  
combined_word_counts_palestine.pop('', None)  
#visualize_most_used_words(combined_word_counts_west, top_n=20, title='Western Sources')
#visualize_most_used_words(combined_word_counts_palestine, top_n=20, title='Palestine Sources')



# creates a side by side graph of the most used words 
def combined_hist():
    'creates a combined histogram using the pickled dictionaries'
    df1 = pd.DataFrame(list(combined_word_counts_west.items()), columns=['Word', 'Count'])
    df2 = pd.DataFrame(list(combined_word_counts_palestine.items()), columns=['Word', 'Count'])
    # Sort by 'Count' and take the top 30 for each DataFrame
    df1_top = df1.sort_values(by='Count', ascending=False).head(30)
    df2_top = df2.sort_values(by='Count', ascending=False).head(30)
    df_top = df1_top.set_index('Word').join(df2_top.set_index('Word'), lsuffix='_west', rsuffix='_palestine', how='outer')
    df_top.plot.bar(stacked=False, figsize=(10,7))
    plt.title('Top 30 Word Frequency Comparison')
    plt.xlabel('Words')
    plt.ylabel('Count')
    plt.show()

def main(): 
    visualize_most_used_words(combined_word_counts_west, top_n=20, title='Western Sources')
    visualize_most_used_words(combined_word_counts_palestine, top_n=20, title='Palestine Sources')
    combined_hist()


if __name__ == '__main__':
    main()






















