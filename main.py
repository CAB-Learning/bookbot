def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted = sort_chars_dict(chars_dict)
    report(book_path, num_words, chars_sorted)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()

def sort_chars_dict(num_chars_dict):
    sorted_list=[]
    for ch in num_chars_dict:
        sorted_list.append({"char" : ch, "num": num_chars_dict[ch]})  
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def report(book_path, num_words, char_sorted):
    print (f"--- Begin report of {book_path} ---")
    print (f"{num_words} words found in the document")
    for slot in char_sorted:
        if not slot["char"].isalpha():  ## added to filter out non-letters
            continue
        print(f"The '{slot['char']}' character was found {slot['num']}' times'")
    print ("--- End report ---")

def sort_on(dict):
    return dict["num"]

main()