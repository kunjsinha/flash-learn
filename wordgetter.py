import random

def load_words():
    with open("wordsdataset.txt", "r") as f:
        words = f.read().splitlines()
    return words

def get_random_word(count):
    words = load_words()
    return random.sample(words, count)