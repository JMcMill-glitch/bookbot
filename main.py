import sys
from stats import count_of_words, count_of_characters, report_of_dictionary

def main():
    if len(sys.argv) == 2:
        text = get_book_text(sys.argv[1])
        word_count = count_of_words(text)
        count_of_chars = count_of_characters(text)
        printed_dict = report_of_dictionary(count_of_chars)
        print(f"============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}")
        print(f"----------- Word Count ----------")
        print(word_count)
        print(f"--------- Character Count -------")
        for dict in printed_dict:
            print(f"{dict["key"]}: {dict["value"]}")
        print(f"============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

         

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()