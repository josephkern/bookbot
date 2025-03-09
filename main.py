from stats import word_count, character_count, char_count_report

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content

def main():
    
    book = "books/frankenstein.txt"

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
