from fuzzywuzzy import fuzz
import part1 as p


# print(fuzz.ratio("this is a test", "this is a test!")) # 97
# print(fuzz.partial_ratio("this is a test", "this is a test!")) # 100
# print(fuzz.ratio("fuzzy wuzzy was a bear", "wuzzy fuzzy was a bear")) # 91
# print(fuzz.token_sort_ratio("fuzzy wuzzy was a bear", "wuzzy fuzzy was a bear")) # 100

if __name__ == "__main__":
    cf = p.Cuba_freedom
    hc = p.history_Cuba
    mmp = p.murder_piracy

    #Fuzz Ratio is good for identifying the overall similarity of the two strings. The higher the score the more similar they are
    #print("CF vs HC ratio:", fuzz.ratio(cf, hc))  # 44
    #print("CF vs MMP ratio:", fuzz.ratio(cf, mmp))  # 45

    #The Token Set Ratio algorithm tokenizes both input strings, removes duplicate tokens, and calculates the similarity score based on the intersection and union of the token sets. It captures the essence of the strings’ content rather than their specific order.
    #The pirate book was much more similar to the book about Cuba's fight for freedom than I expected
    print("CF vs HC token_sort_ratio:", fuzz.token_set_ratio(cf, hc))  #80 
    print("CF vs MMP token_sort_ratio:", fuzz.token_set_ratio(cf, mmp))  #76 
