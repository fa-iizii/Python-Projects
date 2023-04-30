import random
import string

# Define some ASCII art to use in the UI
title_art = """

╔═══╗────────────────────╔╗
║╔═╗║────────────────────║║
║╚═╝╠══╦══╦══╦╗╔╗╔╦══╦═╦═╝║
║╔══╣╔╗║══╣══╣╚╝╚╝║╔╗║╔╣╔╗║
║║──║╔╗╠══╠══╠╗╔╗╔╣╚╝║║║╚╝║
╚╝──╚╝╚╩══╩══╝╚╝╚╝╚══╩╝╚══╝
╔═══╗─────────────╔╗
║╔═╗║────────────╔╝╚╗
║║─╚╬══╦═╗╔══╦═╦═╩╗╔╬══╦═╗
║║╔═╣║═╣╔╗╣║═╣╔╣╔╗║║║╔╗║╔╝
║╚╩═║║═╣║║║║═╣║║╔╗║╚╣╚╝║║
╚═══╩══╩╝╚╩══╩╝╚╝╚╩═╩══╩╝                      
"""

password_art = """
© © © © © © © © © © © © © © 

╔╗───╔═╗────╔╦╦═╦╦╗
║╚╦╦╗║═╬═╦══╬╬╬═╠╬╣
║╬║║║║╔╣╬╚╦═╣║║═╣║║
╚═╬╗║╚╝╚══╝─╚╩╩═╩╩╝
──╚═╝
"""


# Print the title ASCII art
print(title_art)

# Print the password ASCII art
print(password_art)
    
def generate_password(length, uppercase, lowercase, digits, special_chars):
    """
    Generates a random password of the specified length and character set.
    """
    # Define the character set based on user input
    character_set = ''
    if uppercase:
        character_set += string.ascii_uppercase
    if lowercase:
        character_set += string.ascii_lowercase
    if digits:
        character_set += string.digits
    if special_chars:
        character_set += string.punctuation

    # Generate the password
    password = ''.join(random.choice(character_set) for i in range(length))
    return password

# Get user input for password length and character set
length = int(input("Enter the length of the password: "))
uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
digits = input("Include digits? (y/n): ").lower() == 'y'
special_chars = input("Include special characters? (y/n): ").lower() == 'y'

# Generate and print the password
password = generate_password(length, uppercase, lowercase, digits, special_chars)
print(f"Your password is: {password}")
