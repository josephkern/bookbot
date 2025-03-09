from stats import word_count, character_count, char_count_report

import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content

def main():
    
    # System Arguments
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book_>")
        sys.exit(1)
    else:
        book = sys.argv[1]

    #book = "books/frankenstein.txt"
    
    raw_text = get_book_text(book)
    #print(f'{raw_text}')
    #Print Title
    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {book}...')
    # print word count title
    print("----------- Word Count ----------")
    print(f'Found {word_count(raw_text)} total words')
    # print character count tile
    print("--------- Character Count -------")
    char_report_data = char_count_report(character_count(raw_text))
    for char_report in char_report_data:
        #for i in char_report.items():
        print(f'{char_report["char"]}: {char_report["num"]}')
    #print(character_count(raw_text))
    print("============= END ===============")

main()
