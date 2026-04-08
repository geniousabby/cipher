"""
Encript or decript using the affine cipher.

"""


# Welcome user to the program
def start():
    """
    Welcomes user and gets their name.

    """

    name = input("What is your name?: ").strip().title()
    print(f"Welcome to the Affine Code Decipher Program, {name}!")


# Print definition of the cipher
def define():
    """
    Explains what the cipher does.
    
    """

    print("\nTHE AFFINE CIPHER:")

    print("\nThe Affine Cipher is a cipher that uses math to encode the message. " \
    "It works by converting every letter in the alphabet " \
    "into a number and performing a function on that number.")

    print("For example, the letter 'a' is the " \
    "number '1' since it's the first number in the alphabet.")


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
        print("\n1- Define the cipher")
        print("2- Decrypt")
        print("3- Encrypt")
        print("4- Exit")

        # Ask user for their choice
        choice = input("\nWhat would you like to do? ")

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
