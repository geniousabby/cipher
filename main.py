"""
Encript or decript using the affine cipher.

"""


# Welcome user to the program
def start():
    """
    Welcomes user and gets their name.

    """



# Print definition of the cipher
def define():
    """
    Explains what the cipher does.
    
    """


# Ask user if they want to decrypt
def decrypt():
    """
    Decrypts the message entered by the user
    
    """


# Ask user if they want to encrypt
def encrypt():
    """
    Encrypts the message entered by the user.
    
    """


# Print message


def main():
    """
    Main function that calls the other functions.

    """

    # Run start function
    start()

    while True:

        # Print options
        print("1- Define the cipher")
        print("2- Decrypt")
        print("3- Encrypt")
        print("4- Exit")

        # Ask user for their choice
        choice = input("\nWhat would you like to do?")

        if choice == "1":
            define()

        elif choice == "2":
            decrypt()

        elif choice == "3":
            encrypt()

        elif choice == "4":
            print("Thanks for playing!")
            break





if __name__ == "__main__":
    main()
