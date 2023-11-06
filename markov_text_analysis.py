from collections import defaultdict
import part1 as p

# research link: https://observablehq.com/@dhowe/tut-rita-ngrams 
#Chat GPT link: https://chat.openai.com/share/cc46d90a-37af-44e4-b73c-4cbc263a3ad2 
def build_markov_chain(text, n):
    """This builds the actual "chain". The n is the amount of consecutive words that are brought together
    """
    words = text.split()
    chain = defaultdict(list)

    for i in range(len(words) - n):
        ngram = tuple(words[i : i + n])
        next_word = words[i + n]
        chain[ngram].append(next_word)

    return chain


import random


def generate_text(chain, n, max_words):
    current_ngram = random.choice(list(chain.keys()))
    text = list(current_ngram)

    while len(text) < max_words:
        next_word = random.choice(chain[current_ngram])
        text.append(next_word)
        current_ngram = tuple(text[-n:])

    return " ".join(text)


# Load your source text
cf = p.Cuba_freedom
mmp = p.murder_piracy
hc = p.history_Cuba


def text_generation(source_text, n_size):
    # Build the Markov chain
    n = n_size # You can adjust the n-gram size
    markov_chain = build_markov_chain(source_text, n)

    # Generate text
    generated_text = generate_text(markov_chain, n, 100)  # 100 words in this example

    return generated_text

print(f"MMP n-size 1: {text_generation(mmp,1)}")
print()
print(f"MMP n-size 5: {text_generation(mmp,1)}")
print()
print(f"MMP n-size 15: {text_generation(mmp,1)}")

