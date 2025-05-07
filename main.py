from stats import get_number_of_words
from stats import get_count_of_characters
from stats import sort_on
import sys
def main():
    if len(sys.argv) < 2 :
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    get_text = get_book_text(sys.argv[1])
    number = get_number_of_words(get_text)
    print(f"Found {number} total words")
    
    #print(get_count_of_characters(get_text))
    get_characters = get_count_of_characters(get_text)
    
    characters =  sort_on(get_characters)
    for char in characters:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")
        
    #return sort_on(get_characters)



def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
        


main()



"""
#Solution of the original

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
"""

