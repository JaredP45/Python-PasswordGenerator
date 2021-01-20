"""
+---------------------------------------------------------+
|   Author: Jared Paubel                                  |
|   Organisation: Self                                    |
|   Date: 01-19-2021                                      |
+---------------------------------------------------------+
"""
import random
import string
from tkinter import *



def pass_generator():
    """
    - Create empty string
    - 1st for loop generates a string of 4 elements out of each ascii value
    - 2nd for loop generates a random string of the length entered by user minus (-) 4
    - Add to password variable. Subtract 4 due to 4 already being established by 1st for loop
    """

    password = ''  # Initialized as empty
    for x in range(0, 4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(
            string.digits) + random.choice(string.punctuation)
    for y in range(pass_len.get() - 4):
        password = password + random.choice(
            string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)

    pass_str.set(password)  # Set password to pass_str (holds the generated password)


# PassGen window
root = Tk()  # Initialize tkinter
root.geometry("400x400")  # Set w/h
root.resizable(0, 0)  # Set window as fixed
root.title("Jared's PassGen")  # set title

# Label() is used to display lines of text which users cannot modify
# root is name referring to the window that loads
Label(root, text='PASSWORD GENERATOR', font='arial 15 bold').pack()
Label(root, text='Jared', font='arial 15 bold').pack(side=BOTTOM)

# Spinbox() is used to select from a fixed amount of numbers
pass_len = IntVar()  # Used to store the length of a password
pass_label = Label(root, text='PASSWORD LENGTH', font='arial 10 bold').pack()
length = Spinbox(root, from_=8, to_=32, textvariable=pass_len, width=15).pack()

# Button accesses pass_generator function, and generates password
Button(root, text="GENERATE PASSWORD", command=pass_generator).pack(pady=5)

# Entry posts the password into text box
pass_str = StringVar()  # Initialized, and used to store the generated password
Entry(root, textvariable=pass_str).pack()
root.mainloop()

# END-OF-FILE