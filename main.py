from stats import get_num_words

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    file_string = get_book_text("books/frankenstein.txt")
    
    word_count = get_num_words(file_string)

    print(f"{word_count} words found in the document")


main()
