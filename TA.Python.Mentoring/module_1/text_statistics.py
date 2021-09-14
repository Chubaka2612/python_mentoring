from collections import Counter


def word_count(search_word, text):
    return get_words(text).count(search_word)


def max_letter(text):
    letters = "".join(map(str, get_words(text)))
    return Counter(letters).most_common(1)


def get_words(text):
    text = text.replace("\n", " ")
    text = text.replace(",", "").replace(".", "").replace("-", "").replace("!", "")
    words = text.lower().split()
    return words


def show_statistics(search_word, text):
    print("Search word:", search_word, " count:", word_count(search_word, text))
    print("Popular letter:", max_letter(text))