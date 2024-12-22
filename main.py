def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


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


main()


"""def main():
    with open("books/frankenstein.txt") as f:
        text = f.read()
    
    def check_if_alpha():
        alfa_string = ""
        for char in text:
            if char.isalpha:
                alfa_string += char
        print(alfa_string)
                
    
    print(len(text.split()))

    char_dic = {}
    
    lower_case_chars = text.lower()
    unique_chars = set(lower_case_chars)
 
    stat = {c:text.count(c) for c in unique_chars}
    print(stat)
    
    

if __name__ == '__main__':
    main() """
