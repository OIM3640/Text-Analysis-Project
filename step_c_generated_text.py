# Anslysis #2: This part uses Markov model to generate new film reviews
# based on the previous scraped film reviews
"""
This module contains utility functions for processing text data.
"""
import random
import re


def generate_markov_model(text, order=1):
    """
    Generate a Markov model of a text based on 
    conditional probabilities of each word given preceding words.

    Args:
        text (str): The input text file as a string.
        order (int, optional): The order of the Markov model, 
        i.e., the number of preceding words to consider for each word. Defaults to 1.

    Returns:
        dict: The Markov model as a dictionary of dictionaries, 
        where the outer keys are tuples of `order` words, 
        and the inner keys are words that follow the corresponding prefix in the text, 
        and the values are the transition probabilities.

    """
    # Split the text into words and lowercase them
    words = re.findall(r'\w+', text.lower())

    # Initialize the Markov model as a dictionary of dictionaries
    model = {}
    for i in range(len(words) - order):
        prefix = tuple(words[i:i+order])
        suffix = words[i+order]
        if prefix in model:
            if suffix in model[prefix]:
                model[prefix][suffix] += 1
            else:
                model[prefix][suffix] = 1
        else:
            model[prefix] = {suffix: 1}

    # Normalize the transition probabilities for each prefix
    for prefix in model:
        total_count = sum(model[prefix].values())
        for suffix in model[prefix]:
            model[prefix][suffix] /= total_count

    return model


def generate_text(model, length=100):
    """
    Generate a new text using a given Markov model of a text file.

    Args:
        model (dict): The Markov model as a dictionary of dictionaries, 
                      where the outer keys are tuples of `order` words, 
                      and the inner keys are words that follow the corresponding prefix in the text, 
                      and the values are the transition probabilities.
        length (int, optional): The length of the generated text in number of words. 
                                sDefaults to 100.

    Returns:
        str: The generated text as a string.

    """
    # Choose a random starting prefix from the model
    prefix = random.choice(list(model.keys()))

    # Generate a new text using the Markov chain
    text = list(prefix)
    for i in range(length - len(prefix)):
        suffix_probs = model[prefix]
        suffix = random.choices(list(suffix_probs.keys()),
                                weights=list(suffix_probs.values()))[0]
        text.append(suffix)
        prefix = tuple(text[-len(prefix):])

    return ' '.join(text)


def main():
    """
    This is the main function: film reviews for Stranger Things and Vampire Diaries are generated 
    """
    # Generated film review for Stranger Things
    with open('stranger_things_reviews.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    model = generate_markov_model(text, order=2)
    generated_text_strangr_things = generate_text(model, length=100)
    print(generated_text_strangr_things)
    # Generated film review for Vampire Diaries
    with open('vampire_diaries_reviews.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    model = generate_markov_model(text, order=2)
    generated_text_vampire_diaries = generate_text(model, length=100)
    print(generated_text_vampire_diaries)


if __name__ == '__main__':
    main()
