import inquirer


# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# Press ⌃R to execute it or replace it with your code.

def menu_selection():
    questions = [
        inquirer.List('menu',
                      message="Please select an option",
                      choices=['Option 1', 'Option 2', 'Option 3'],
                      ),
    ]
    answers = inquirer.prompt(questions)
    return answers['menu']


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
