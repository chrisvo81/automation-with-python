import random
import string
import inquirer
from art import logo
import english_words

# Load the set of English words
english_words_set = english_words.get_english_words_set(sources=['web2'], alpha=True, lower=True)

# Select a random word from the list
def random_word(length=5):
    possible_words = [word for word in english_words_set if len(word) == length]
    return random.choice(possible_words) if possible_words else ''

#
def generate_words(num_words):
    words = []
    for i in range(num_words):
        word_length = int(input(f"Enter the length of word {i+1}: "))
        words.append(random_word(word_length))
    return words

# Main function
def main():
    print(logo)
    print("Welcome to the PyPassword Generator!")
    print("This program will generate a random password for you.")

    # Get number of words they want in the password
    num_words = int(input("How many words would you like in your password? "))
    words = generate_words(num_words)
    print("words", words)

    # Get the number of digits they want in the password
    num_digits = int(input("How many digits would you like in your password? "))
    digits = random.choices(string.digits, k=num_digits)
    print("digits", digits)

    # Choose the set of special characters they want in the password
    custom_sp_chars = "!@#$%^&*-_.+?"
    string_punctuation = string.punctuation
    print()
    chars_set_question = [inquirer.List('special_chars',
                  message="Choose the special characters you want in your password",
                  choices=[custom_sp_chars, string_punctuation],
                  ), ]
    selected_chars_set = inquirer.prompt(chars_set_question)["special_chars"]

    # Get the number of symbols they want in the password
    num_symbols = int(input("How many symbols would you like in your password? "))
    symbols = random.choices(selected_chars_set, k=num_symbols)
    print("symbols", symbols)



if __name__ == '__main__':
    main()