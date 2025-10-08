from stats import word_count, char_count
import sys

def get_book_text(title):
    with open (f"./books/{title}.txt", "r") as file:
        text = file.read()
    return(text)

def main():
    try:
        if len(sys.argv) != 2:
            print('Usage: python3 main.py <path_to_book>')
            sys.exit(1)
        title = sys.argv[1]
        print('============ BOOKBOT ============')
        print(f'Analyzing book found at {title}...')
        print('----------- Word Count ----------')
        print(f'Found {word_count(title)} total words')
        print('-------- Character Count --------')
        char_dict = list(char_count(title).items())
        char_dict.sort(key=lambda x: x[1], reverse=True)
        for item in char_dict:
            print(f'{item[0]}: {item[1]}')
    except FileNotFoundError:
        print(f'Error: Book at "{sys.argv[1]}" not found.')
        sys.exit(1)

main()