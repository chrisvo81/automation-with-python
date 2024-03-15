import random
import string
from art import logo
# from wordlist import SimpleWordlist  # Ensure this is the correct import
import wordlist
import english_words

# Load the set of English words
english_words_set = english_words.get_english_words_set(sources=['web2'], alpha=True, lower=True)

# Select a random word from the list
def random_word():
    list_of_words = english_words_set
    print(list_of_words)

# Main function
def main():
    print(logo)
    print("Welcome to the PyPassword Generator!")
    print("This program will generate a random password for you.")
    random_word()


if __name__ == '__main__':
    main()