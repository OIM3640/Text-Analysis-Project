# Text-Analysis-Project

Please read the [instructions](instructions.md).



**IMDB Review Similarity for Beginners**

## 1. Project Overview

This project compares user reviews on four well-known movies using simple natural language processing in Python. We want to analyze how similar reviews are with respect to the words users use to describe a movie.

**Films Used**  
- The Dark Knight  
- Inception  
- Interstellar  
- Avengers: Endgame  

We gathered review text with the `cinemagoer` (IMDB) library and processed them with TF-IDF and cosine similarity.

## 2. How It Works

The project is divided into four simple files:

- `fetch_reviews.py`: Download up to 20 reviews per movie and save them to text files.  
- `utils.py`: This cleanses the text by eliminating punctuation, lowercasing it, and deleting frequent stop words.  
- `analyze_similarity.py`: This loads the text data, converts them to word vectors with TF-IDF and measures the similarity between each movie's reviews based on cosine similarity. It prints the similarity scores in an easily readable manner.  
- `main.py`: A straightforward script to execute everything sequentially: it fetches the reviews and then compares them.  

We employed plain readable code and straightforward loops to maintain beginner-friendliness.

## 3. Results

Upon executing the code, you will observe the following output:

```
Movie Review Similarity Scores (0 = not similar, 1 = very similar):

The Dark Knight ⇌ Inception: 0.50  
The Dark Knight ⇔ Interstellar: 0.48  
The Dark Knight vs Avengers Endgame: 0.28  
Inception ↔ Interstellar: 0.61  
Inception ↔ Avengers Endgame: 0.32  
Interstellar ↔ Avengers Endgame: 0.30
```

From this we can observe:  
- **Inception** and **Interstellar** share the most similar reviews (0.61).  
- **Avengers: Endgame** has more distinctive individual reviews than the rest of the franchise.  

These variations probably indicate the tone, subject matter, and audience of the movies.

## 4. Reflection

### What Went Well  
- Using the IMDB API was easy with the `cinemagoer` package.  
- Breaking the project into small files made it manageable.  
- Cleaning the text and similarity calculation resulted in significant outcomes.  

### What Was Hard  
- Understanding the working of TF-IDF and cosine similarity.  
- Ensuring that the text was cleaned correctly prior to being compared.  

### What I Learned  
- How to process real-world text data with Python.  
- How to convert words into numbers (TF-IDF) to compare documents.  
- How to maintain my code clean and beginner-friendly.  

### How GenAI Helped  
I used ChatGPT to:  
- Describe TF-IDF and cosine similarity  
- Propose a modular file structure  
  

## 🔧 How to Run This Project

### Step 1: Install Python libraries  
Make sure that the following are installed:  

```bash
pip install imdbpy nltk scikit-learn
```

### Step 2: Run the main file  
This will retrieve reviews and evaluate similarities:  

```bash
python main.py
```

It can take a few seconds to load reviews from IMDB the first time.

