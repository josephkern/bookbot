from stats import word_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content

def main():
    
    raw_text = get_book_text("books/frankenstein.txt")
    print(f'{word_count(raw_text)} words found in the document')
    #print(f'{raw_text}')

main()
