import os


def main():
    with open('My Clippings.txt', 'r', encoding='utf-8-sig') as f:
        content = f.read().splitlines()
    book_clippings = get_book_clippings_dict(content)
    write_clippings(book_clippings)


def write_clippings(book_clippings):
    if not os.path.exists('books'):
        os.makedirs('books')
    for key, value in book_clippings.items():
        if key != 'my_book':
            with open('books/{}.txt'.format(key), 'w') as f:
                f.write(value)


def get_book_clippings_dict(content):
    book_clippings = {}
    current_book = None
    for line in content:
        if line is None or line == '':
            pass
        elif current_book is None:
            current_book = line.replace('\ufeff', '')
        elif line == '==========':
            current_book = None
        else:
            if current_book in book_clippings:
                book_clippings[current_book] += line + '\n'
            else:
                book_clippings[current_book] = line + '\n'
    return book_clippings


if __name__ == '__main__':
    main()
