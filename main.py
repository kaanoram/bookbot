def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print("--- Begin report of books/frankenstein.txt ---")
    num_words = count_words(text)
    print(f"{num_words} words found in the document")
    letter_counts = count_letters(text)
    report_letters(letter_counts)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_letters(text):
    counter = {}
    for char in text.lower():
        if char.isalpha():
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1
    return counter

def sort_on(d):
    return d['count']

def report_letters(letter_dict):
    letter_list = [{"char": key, "count": value} for key, value in letter_dict.items()]
    letter_list.sort(reverse = True, key = sort_on)
    for letter in letter_list:
        print(f"The '{letter['char']}' character was found {letter['count']} times")



main()