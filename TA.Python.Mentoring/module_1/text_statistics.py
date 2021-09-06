from collections import defaultdict
import min_max


def word_count(search_word, text):
    word_list = get_words(text)
    word_count_dict = defaultdict(int)
    for word in word_list:
        word_count_dict[word] += 1
    return word_count_dict[search_word]


def max_letter(text):
    words = get_words(text)
    letter_count_dict = defaultdict(int)
    for word in words:
        for char in word:
            letter_count_dict[char] += 1
    max_count = min_max.find_max(letter_count_dict.values())
    max_count_letter = get_key_by_value(max_count, letter_count_dict)

    return max_count_letter, max_count


def get_words(text):
    text = text.replace("\n", " ")
    text = text.replace(",", "").replace(".", "").replace("-", "").replace("!", "")
    words = text.lower().split()
    return words


def show_statistics(search_word, text):
    max_count_letter, max_count = max_letter(text)
    print("Search word:", search_word, " count:", word_count(search_word, text))
    print("Popular letter:", max_count_letter, " count:", max_count)


def get_key_by_value(value, test_dict):
    return list(test_dict.keys())[list(test_dict.values()).index(value)]
