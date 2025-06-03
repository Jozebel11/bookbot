def get_book_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(f"{len(file_contents.split())} words found in the document")

def main():
    get_book_text()

main()