from stats import word_count, letter_count, sorted_list
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    book_text = get_book_text(path)
    num_words = word_count(book_text)

    letter_counts = letter_count(book_text)
    sorted_letters = sorted_list(letter_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for letter_item in sorted_letters:
        if letter_item["letter"].isalpha():
            print(f"{letter_item['letter']}: {letter_item['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
