from mediawiki import MediaWiki
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import networkx as nx
from itertools import combinations

#Get Wikipedia Text
wikipedia = MediaWiki()
Panama = wikipedia.page("Panama")
text = Panama.content

# Text Preprocessing
# nltk.download('punkt')
# nltk.download('stopwords')

def preprocess_text(text):
    sentences = sent_tokenize(text)
    words = [word for word in word_tokenize(text) if word.isalnum()]
    words = [word.lower() for word in words]
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word not in stop_words]
    return sentences, words

sentences, words = preprocess_text(text)

#Building a Graph
def build_sentence_graph(sentences, threshold=0.2):
    G = nx.Graph()

    for sentence1, sentence2 in combinations(sentences, 2):
        words1 = set(sentence1.split())
        words2 = set(sentence2.split())
        common_words = words1 & words2
        if len(common_words) > 0:
            similarity = len(common_words) / (len(words1) + len(words2))
            if similarity > threshold:
                G.add_edge(sentence1, sentence2, weight=similarity)

    return G

sentence_graph = build_sentence_graph(sentences)

#Rank Sentences
scores = nx.pagerank(sentence_graph, weight='weight')

#Generate Summary
num_sentences_in_summary = 5
sorted_sentences = sorted(scores, key=scores.get, reverse=True)
summary = " ".join(sorted_sentences[:num_sentences_in_summary])
print(summary)
