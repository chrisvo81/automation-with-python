import random
import string
import inquirer
from art import logo
import english_words

# Load the set of English words
english_words_set = english_words.get_english_words_set(sources=['web2'], alpha=True, lower=True)

# Global store for reusable user selections
user_selection = {
    "words": {
        "set": [], # set of length for each words
        "length": 0 # number of words
    },
    "digits": 0,
    "special_chars": {
        "set": "", # set of special characters
        "length": 0 # number of special characters
    }
}


# Select a random word from the list
def random_word(length=5):
    possible_words = [word for word in english_words_set if len(word) == length]
    return random.choice(possible_words) if possible_words else ''


# Generate random words
def generate_words(num_words):
    words = []
    for i in range(num_words):
        word_length = int(input(f"Enter the length of word {i+1}: "))
        words.append(random_word(word_length))
    return words


# Select a set of special characters
def select_set_of_special_chars():
    custom_sp_chars = "!@#$%^&*-_.+?"
    string_punctuation = string.punctuation
    print()
    chars_set_question = [inquirer.List('special_chars',
                  message="Choose the special characters you want in your password",
                  choices=[custom_sp_chars, string_punctuation],
                  ), ]
    selected_chars_set = inquirer.prompt(chars_set_question)["special_chars"]
    user_selection["special_chars"]["set"] = selected_chars_set
    return selected_chars_set


# Prompt for input, return number
def prompt_for_input(prompt):
    num = int(input(f"How many {prompt} would you like in your password?\n"))
    if prompt != "digits":
        user_selection[prompt]["length"] = num
    else:
        user_selection[prompt] = num
    return num


# Generate random password
def generate_random_password(words=[], digits=[], special_chars=[]):
    # Shuffle words, digits, and special chars independently
    random.shuffle(words)
    random.shuffle(digits)
    random.shuffle(special_chars)

    # Create a pattern for how words, digits, and special chars should be combined
    # Ensuring that words are more likely to remain together for readability
    pattern = words + digits + special_chars

    # Shuffle the pattern to mix the types while keeping the words intact
    random.shuffle(pattern)

    # Join everything to form the password
    return ''.join(pattern)


# Gather user input
def gather_user_input():
    # Get number of words they want in the password
    num_words = prompt_for_input("words")
    words = generate_words(num_words)
    print("words", words)

    # Get the number of digits they want in the password
    num_digits = prompt_for_input("digits")
    digits = random.choices(string.digits, k=num_digits)
    print("digits", digits)

    # Choose the set of special characters they want in the password
    selected_chars_set = select_set_of_special_chars()

    # Get the number of symbols they want in the password
    num_symbols = prompt_for_input("special_chars")
    symbols = random.choices(selected_chars_set, k=num_symbols)
    print("symbols", symbols)

    return {
        "words": words,
        "digits": digits,
        "special_chars": symbols
    }


# Main function
def main():
    print(logo)
    print("Welcome to the PyPassword Generator!")
    print("This program will generate a random password for you.")

    generated_list = gather_user_input()
    print(user_selection)

    final_password = generate_random_password(generated_list["words"], generated_list["digits"],
                                              generated_list["special_chars"])

    print("final_password", final_password)


if __name__ == '__main__':
    main()