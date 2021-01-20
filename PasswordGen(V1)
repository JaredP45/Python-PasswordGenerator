import random


def passwordGen():
    """
    This password generator goes into a loop, and will continue to scramble passwords based on users
    desired length until the user enters 0 to exit.
    """

    # Set string with characters desired for password
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&amp;*1234567890"
    length = int(input("Enter Password length\n>> "))

    while length != 0:
        password = ""
        for i in range(length):
            password += random.choice(characters)
        print(password)

        length = int(input("Would you like to continue, or quit? (0 to quit)\n>> "))
    print("Thanks for using my password generator!")


passwordGen()
# END-OF-FILE
