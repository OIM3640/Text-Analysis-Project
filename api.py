import os
import json
from dotenv import load_dotenv
from openai import OpenAI

# load .env and get key
load_dotenv()
if "OPENAI_API_KEY" not in os.environ:
    raise RuntimeError("Please set OPENAI_API_KEY in a .env file or as an environment variable.")

client = OpenAI()

# stopwords tailored to Iliad / Odyssey style text
STOPWORDS = {
    # core English
    "the", "and", "to", "of", "a", "in", "that", "it", "is", "was", "for",
    "on", "with", "as", "by", "this", "but", "from", "or", "not", "are",
    "at", "be", "an", "which", "so", "we", "were", "have", "has", "had",

    # pronouns
    "i", "you", "he", "she", "they", "them", "their", "theirs", "his",
    "her", "hers", "him", "me", "my", "mine", "our", "ours", "us", "your",
    "yours", "who", "whom", "whose",

    # connectors / often-seen words
    "what", "when", "where", "why", "how", "then", "now", "there", "here",
    "thus", "all", "one",

    # helper verbs
    "shall", "will", "would", "may", "might", "can", "could", "must", "should",

    # archaic
    "thy", "thou", "thee", "ye", "o", "unto", "doth", "hath",

    # dialogue
    "said", "say", "says",

    # iterated words from testing
    "no", "nor", "more", "these", "some", "yet", "o'er", "come", "own", "into", "if", "went", "been", "up",
    "out", "do", "about", "one", "man", "us", "went", "go", "upon", "men", "did", "tell", "see", "any", "made",
    "other", "good", "much", "back",

    # stray unicode
    "“", "”", "—"
}


def extract_entities_with_openai(text):
    """
    Call OpenAI to get characters / places / gods from a passage.
    """
    prompt = (
        "You will be given a passage from Homer (Iliad or Odyssey). "
        "Extract the names of characters, places, and gods that are explicitly mentioned. "
        "Return ONLY valid JSON like this:\n"
        "{\n"
        '  \"characters\": [\"Achilles\"],\n'
        '  \"places\": [\"Troy\"],\n'
        '  \"gods\": [\"Athena\"]\n'
        "}\n"
        "If none are found, return empty lists.\n\n"
        "Passage:\n" + text
    )

    resp = client.chat.completions.create(
        model="gpt-5-nano",
        messages=[
            {"role": "system", "content": "You extract entities from classical literature and return strict JSON."},
            {"role": "user", "content": prompt}
        ],
        temperature=1
    )

    content = resp.choices[0].message.content
    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        data = {"characters": [], "places": [], "gods": []}
    return data


def tally_entities(all_passage_entities):
    """
    Combine entity dicts into frequency dicts.
    """
    char_counts = {}
    place_counts = {}
    god_counts = {}

    for ent in all_passage_entities:
        for c in ent.get("characters", []):
            c = c.strip()
            if c:
                char_counts[c] = char_counts.get(c, 0) + 1
        for p in ent.get("places", []):
            p = p.strip()
            if p:
                place_counts[p] = place_counts.get(p, 0) + 1
        for g in ent.get("gods", []):
            g = g.strip()
            if g:
                god_counts[g] = god_counts.get(g, 0) + 1

    return char_counts, place_counts, god_counts