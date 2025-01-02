def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(f"--- Begin report of {book_path} ---")
    print(f"{count_words(text)} was found in the document\n")
    # print(f"{get_chars_dic(text)}")
    print_chars_dic(text)
    print(f"--- End report ---")

def get_chars_list(dict):
    """Return a list with a dictionary for each character."""
    chars = []
    for c in dict:
        chars.append({"char": c, "times": dict[c]})
    return chars

def print_chars_dic(text):
    """Print all elements in the dictionary ordered from most to least frequent."""
    chars_dict = get_chars_dic(text)
    chars = get_chars_list(chars_dict)
    chars.sort(reverse=True, key=lambda chars: chars["times"])
    for ch in chars:
        if ch["char"].isalpha():
            print(f"The {ch["char"]} character was found {ch["times"]} times")
    
def get_chars_dic(text):
    """Return an unordered dictionary of all characters in the book."""
    chars = {}
    for character in text:
        low_char = character.lower()
        if low_char in chars:
            chars[low_char] += 1
        else:
            chars[low_char] = 1
    return chars
    
def count_words(book):
    """Count words in the book passed."""
    words = book.split()
    return len(words)

def get_book_text(path):
    """Return all text in the book."""
    with open(path) as f:
        return f.read()
        
main()