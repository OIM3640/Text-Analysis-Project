# This is the main file to run the whole project

from fetch_reviews import main as get_data
from analyze_similarity import main as analyze_data

if __name__ == "__main__":
    print("Step 1: Getting reviews from IMDB...")
    get_data()
    
    print("\nStep 2: Comparing reviews...")
    analyze_data()
