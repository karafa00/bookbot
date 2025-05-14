from stats import count_words, count_characters, pretty_print
from sys import argv, exit as sys_exit

def get_book_text(filePath):
    with open(filePath) as f:
        return f.read()
    

def main():
    if len(argv) != 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys_exit(1)
    
    filePath = argv[1]
    text = get_book_text(filePath)
    wordCount = len(count_words(text))
    characters = count_characters(text)    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filePath}")
    print("----------- Word Count ----------")
    print(f"Found {wordCount} total words")
    print("--------- Character Count --------")
    pretty_print(characters)
    print("============= END ===============")
main()