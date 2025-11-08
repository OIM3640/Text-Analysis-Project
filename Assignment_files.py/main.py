from download import download_data, clean_file, final_clean_version, remove_stopwords
from analysis import text_summary_statistics, common_words_chart, sentiment_analysis
from translation import create_dictionary, translate_text_file
from similarity import text_similarity


def main(): 
    """ Main function to join the entire diles together and run all of the analysis"""

    print ("\n   Text Analysis \n")

    url = 'https://www.gutenberg.org/cache/epub/1513/pg1513.txt'
    raw_file = download_data(url)
    if not raw_file: 
        return 
        
    clean_file(raw_file, "cleaned_text.txt")
    final_clean_version("cleaned_text.txt")
    remove_stopwords("final_cleaned.txt")

    text_summary_statistics("final_cleaned.txt")
    common_words_chart("final_cleaned.txt")
    sentiment_analysis("final_cleaned.txt")

    dictionary = create_dictionary("development/Dictionary.txt")
    translate_text_file("final_cleaned.txt","translated_text.txt", dictionary)

    text_similarity("final_cleaned.txt", "translated_text.txt")

    print ("\n End of Analysis \n")

if __name__ == "__main__":
    main()