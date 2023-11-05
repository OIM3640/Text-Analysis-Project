1.) Project Overview:

I used the book, “The Great Gatsby” from gutenberg.org. I used a process that was similar to the one that we had used in the past during class. I thought this book would be very interesting since it had only recently entered the public domain, but it is a very significant book that is read by many. 

2.) Implementation

For implementation I followed a lot of what we had done in the past but I wanted to utilize ChatGPT which is something that I did not try before this assignment. One of the things that I did with ChatGPT was the following: 

-----------------------------------------------------------------------------------------------------------------------------------------------------------
Python code that removes all the text before "*** START OF THE PROJECT GUTENBERG EBOOK THE GREAT GATSBY ***" and also removes all the text after "*** END OF THE PROJECT GUTENBERG EBOOK THE GREAT GATSBY ***" from the link: https://www.gutenberg.org/cache/epub/64317/pg64317.txt
Here's the Python code that removes all the text before and after the desired text:

python
Copy code
import urllib.request

url = "https://www.gutenberg.org/cache/epub/64317/pg64317.txt"

# Download the text from the url
response = urllib.request.urlopen(url)
data = response.read()

# Decode the text as UTF-8
text = data.decode('utf-8')

# Find the start and end strings
start_str = "*** START OF THE PROJECT GUTENBERG EBOOK THE GREAT GATSBY ***"
end_str = "*** END OF THE PROJECT GUTENBERG EBOOK THE GREAT GATSBY ***"

# Remove the text before and after the desired text
start_index = text.find(start_str)
end_index = text.find(end_str)

if start_index != -1 and end_index != -1:
    text = text[start_index:end_index]
    
# Print the resulting text
print(text)

This code downloads the text from the given URL, decodes it as UTF-8, and finds the positions of the start and end strings. Then, it removes all the text before and after the desired text using string slicing. Finally, it prints the resulting text.
-----------------------------------------------------------------------------------------------------------------------------------------------------------


I wanted to try this strategy to see alternate ways to filter out the beginning and end of the book when I put it through my analysis. 

3.) Results

In the project I was able to accomplish the task of seeing what the most common words in the piece were and what the most common words were after removing significant stop words. This was easier after I sued ChatGPT’s recommendation of using delete for he dictionary:

how to remove values from a python dictionary
In Python, you can remove values from a dictionary using the del statement or the pop() method. Here's how to use both of them:

Using the del statement
You can remove a value from a dictionary by using the del statement and specifying the key of the value that you want to remove. Here's an example:

-----------------------------------------------------------------------------------------------------------------------------------------------------------
python
Copy code
# Create a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Remove the value associated with the key 'b'
del my_dict['b']

# Print the updated dictionary
print(my_dict)
In this example, the del statement removes the value associated with the key 'b' from the dictionary my_dict. The resulting dictionary contains only the values associated with the keys 'a' and 'c'.

Using the pop() method
The pop() method removes a value from a dictionary and returns it. You can use it to remove a value by specifying the key of the value that you want to remove. Here's an example:

python
Copy code
# Create a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Remove the value associated with the key 'b' and store it in a variable
removed_value = my_dict.pop('b')

# Print the removed value and the updated dictionary
print("Removed value:", removed_value)
print("Updated dictionary:", my_dict)
In this example, the pop() method removes the value associated with the key 'b' from the dictionary my_dict and stores it in the variable removed_value. The resulting dictionary contains only the values associated with the keys 'a' and 'c'. The print() function is then used to display the removed value and the updated dictionary.
-----------------------------------------------------------------------------------------------------------------------------------------------------------


On top of this I also added the natural language processing element to check the element of the language being used. It was helpful to find the sentiment analysis of the book and one observation I had was that “The Great Gatsby” is a short book so there are a lot of important plot information stored into a small section. This strengthens each part of the book and how it contributes to the overall story.

4.) Reflection

Overall I thought that this assignment was very interesting, but it was also extremely challenging for me. I tried to accomplish as much as I could but it was still very challenging and it was also my first exposure in trying to use ChatGPT. I spent a lot of time trying to figure out how to do each individual part of the assignment but felt that there was a large gap in my knowledge when trying to complete different components. One thing that I wish I could have done was see how the past English relates to current English since this is a book that is older but still very recent in terms of older literature. I wish to continue to learn ChatGPT better because I think that it is a very useful tool, but it is something that I only started using recently.  