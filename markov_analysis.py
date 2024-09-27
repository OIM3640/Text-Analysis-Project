from data_processing import import_file, spam_ham_lists, spam_ham_string
import markovify

def markov_analysis(messages):
    """Use Markov analysis to generate new spam messages using data from existing spam.

    messages: string with paragraph essages.

    returns: string with new spam message.
    """
    # Code source: ChatGPT
    # Text model: state_size parameter specifies order of Markov chain
    text_model = markovify.Text(messages, state_size=2)

    # New text: tries parameter specifies number of attempts to generate sentence
    new_text = text_model.make_sentence(tries=100)

    print(new_text)


def main():
    spam_dict = import_file()
    spam_list, ham_list = spam_ham_lists(spam_dict)
    spam_paragraph = spam_ham_string(spam_list)
    ham_paragraph = spam_ham_string(ham_list)

    markov_analysis(spam_paragraph)
    markov_analysis(ham_paragraph)

if __name__ == '__main__':
    main()