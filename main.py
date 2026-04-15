
"""
Encript or decript using the affine cipher.

"""


# Welcome user to the program
def start():
    """
    Welcomes user and gets their name.

    """

    # Get name and print welcome user
    name = input("What is your name?: ").strip().title()
    print(f"Welcome to the Affine Cypher Program, {name}!")


# Print definition of the cipher
def define():
    """
    Explains what the cipher does.
    
    """

    print("\nTHE AFFINE CIPHER:")

    print("\nThe Affine Cipher is a cipher that uses numbers to encode a message. " \
    "It works by converting every letter in the alphabet " \
    "into a number and swaps each letter in the message to its uniquenumber.")

    print("For example, the letter 'a' is the " \
    "number '1' because it's the first number in the alphabet.")


# Decrypt message
def message_de():
    """
    Decodes the message.
    
    """
    # Get user input for message to decrypt
    message = input("\nWhat message would you like to decrypt? ").lower().strip()

    # Reassign values of numbers

    decrypt = {
        '-1':'a',
        '-2':'b',
        '-3':'c',
        '-4':'d',
        '-5':'e',
        '-6':'f',
        '-7':'g',
        '-8':'h',
        '-9':'i',
        '_10':'j',
        '_11':'k',
        '_12':'l',
        '_13':'m',
        '_14':'n',
        '_15':'o',
        '_16':'p',
        '_17':'q',
        '_18':'r',
        '_19':'s',
        '_20':'t',
        '_21':'u',
        '_22':'v',
        '_23':'w',
        '_24':'x',
        '_25':'y',
        '_26':'z',
    }

    # Replace numbers with letters in dictionary
    for key in decrypt:
        message = message.replace(key, decrypt[key])

    # Print decrypted message
    print(f"\nYour decrypted message is: {message}")


# Encrypt message
def message_en():
    """
    Codes the message.
    
    """

    # Get user input for message to encrypt
    message = input("\nWhat message would you like to encrypt? ").lower().strip()

    # Reassign values of letters
    encrypt = {
        'a':'-1',
        'b':'-2',
        'c':'-3',
        'd':'-4',
        'e':'-5',
        'f':'-6',
        'g':'-7',
        'h':'-8',
        'i':'-9',
        'j':'_10',
        'k':'_11',
        'l':'_12',
        'm':'_13',
        'n':'_14',
        'o':'_15',
        'p':'_16',
        'q':'_17',
        'r':'_18',
        's':'_19',
        't':'_20',
        'u':'_21',
        'v':'_22',
        'w':'_23',
        'x':'_24',
        'y':'_25',
        'z':'_26',

    }

    # Replace letters with numbers in dictionary
    for key in encrypt:
        message = message.replace(key, encrypt[key])

    # Print encrypted message
    print(f"\nYour encrypted message is: {message}")


# Main
def main():
    """
    Main function that calls the other functions.

    """

    # Run start function
    start()

    while True:

        # Print options
        print("\n1- Define the cipher")
        print("2- Decrypt")
        print("3- Encrypt")
        print("0- Exit")

        # Ask user for their choice
        choice = input("\nWhat would you like to do? ")

        if choice == "1":
            define()

        elif choice == "2":
            message_de()

        elif choice == "3":
            message_en()

        elif choice == "0":
            print("Thanks for playing!")
            break

        else:
            print("Invalid input.")


if __name__ == "__main__":
    main()
