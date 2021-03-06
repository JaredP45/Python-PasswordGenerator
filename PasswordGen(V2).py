"""
---------------------------
Author: Jared Paubel      |
Organisation: Self        |
Title: Password Generator |
---------------------------
This is a simple password generator that I made. Will eventually improve it overtime 
to actually allow reliable usage.

"""
import random

def shuffle(word):
    """
    Convert parameter to list, then shuffle, then return shuffled word
    """
    tmpList = list(word)
    random.shuffle(tmpList)
    return ''.join(tmpList)

def passwordGen():
    """
    For each letter, digit, and special, randomize value and then use shuffle function
    """
    # Below will generate a random uppercase letter based on ASCII
    letter1 = chr(random.randint(65, 90))
    letter2 = chr(random.randint(65, 90))
    letter3 = chr(random.randint(65, 90))
    letter4 = chr(random.randint(65, 90))
    digit1 = chr(random.randint(48, 57))
    digit2 = chr(random.randint(48, 57))
    special1 = chr(random.randint(35, 38))
    special2 = chr(random.randint(35, 38))

    # Generate password using all of the letters, in a random order
    password = letter1 + letter2 + letter3 + letter4 + digit1 + digit2 + special1 + special2
    password = shuffle(password)
    print(password)

def ask_user_password():
    """
    Ask user whether they want to generate new password: if so, generate, if not
    break out of loop, and terminate the program
    """
    userInput = str(input("Would you like to reset your password? (Yes/No)\n>> "))

    while True: # Runs as long as user says "Yes" or enters wrong value
        if userInput == "Yes" or userInput == "yes":
            passwordGen()
        elif userInput == "No" or userInput == "no":
            break
        else:
            print('You need to enter the values "Yes" or "No".\n')
        userInput = str(input("Do you want to reset the password again? (Yes/No)\n>> "))

    print("Thanks for using this password generator!")


if __name__ == '__main__':
    ask_user_password()

#END-OF-FILE
