#Converts text into a wordds list - returns word count

def get_num_words(book_text):
    words_list=book_text.split()
    num_words=len(words_list)
    return num_words

#Converts text to lower case for character counting.
def lower_case(book_text):
    lower_text=book_text.lower()
    return lower_text

#Character Counting Dictionary
def char_counts(lower_text):

    #Initialize blank dictionary
    counts={}

    #Iterate through characters in text
    for char in lower_text:
        if char in counts:
            counts[char] +=1 #Increment count if already in dictionary
        else:
            counts[char] = 1 #Initialize count to 1 if first time seen in text. 

    return counts

