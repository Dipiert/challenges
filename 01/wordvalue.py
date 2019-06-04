from string import ascii_uppercase
from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as file:
        words = file.read().splitlines()
    return words

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    value = 0
    for letter in word:
        letter = letter.upper()
        if letter in ascii_uppercase:
            value += LETTER_SCORES[letter]
    return value

def max_word_value(words_list=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    max_value = 0
    if words_list is None:
        words_list = load_words()
    for word in words_list:
        if calc_word_value(word) > max_value:
            max_value = calc_word_value(word)
            max_value_word = word
    return max_value_word

if __name__ == "__main__":
    pass # run unittests to validate
