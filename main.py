#Import from stats.py
from stats import get_num_words
from stats import lower_case
from stats import char_counts
from stats import sort_on


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

    #Sort the characters dictionary
    sorted_dict = sorted(characters.items(),key=lambda kv: kv[1], reverse=True)
    list_of_dicts = [{"char": k, "num":v} for k, v in characters.items()]
    list_of_dicts.sort(key=sort_on, reverse = True)
    print("============BOOKBOT============")
    print(f"Analyzing book found at {filepath}...")
    print("----------Word Count----------")
    print(f"Found {num_words} total words")
    print("----------Character Count----------")
    for item in list_of_dicts:
        print(f"{item['char']}: {item['num']}")

main()


    