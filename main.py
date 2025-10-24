#Import from stats.py
from stats import get_num_words
from stats import lower_case
from stats import char_counts


#Function to read the file and return its contents as a string. 

def get_book_text(file_path):
    """Reads the text from a file and returns it as a string."""
    with open(file_path) as f:
        return f.read()
    
#Main function to use get_book_text and print the book. 

def main():
    """Relative path to frankenstein.txt file"""
    filepath = "books/frankenstein.txt"

    #Get the text of the book
    book_text=get_book_text(filepath)

    #Call get_num_words - imported - from stats.py
    num_words=get_num_words(book_text)

    #Convert text to all lower case
    lower_text = lower_case(book_text)

    #Count characters and build out dictionary. 
    characters = char_counts(lower_text)

    #Print number of words to console
    print(f"Found {num_words} total words")

    #Print character count dictionary
    print(characters)

main()


    