

def remove_words(input_string, stop_words):
    """This was heavily helped with ChatGPT. An input string is taken along with a list of stop words. Then the input string is split into individual words. Then all words that are not considered a stop word are added to another list. This list is joined back together into a string and is returned. 
    ChatGPT link: https://chat.openai.com/share/9048aba5-1abb-4750-9922-a7d7dbb3dd95
    """
    # Split the input string into words
    words = input_string.split()
    
    # Filter out words that are not in the list of words to remove
    filtered_words = [word for word in words if word not in stop_words]
    
    # Join the remaining words back into a string
    result_string = " ".join(filtered_words)
    
    return result_string

# Example usage
if __name__ == "__main__":
    input_string = "This is a sample sentence that contains certain words to remove."
    stop_words = ["is", "that", "to"]
    result = remove_words(input_string, stop_words)
    print(result)
