
"""
 Write a function that accepts a list of items a person wants on a sandwich.
 The function should have one parameter that collects as many items as the function call provides,
 and it should print a summary of the sandwich that's being ordered.
 Call the function three times using a different number of arguments each time.

"""


import string

def affine_encryption(plaintext, A, B):
    """
    W

    """

   # Define the uppercase alphabet.
    alphabet = string.ascii_uppercase

    # Get the length of the alphabet
    m = len(alphabet)

    # Initialize an empty string to store the ciphertext.
    ciphertext = ''

    # Iterate through each character in the plaintext.
    for char in plaintext:

        # Check if the character is in the alphabet.
        if char in alphabet:
            # If it's an alphabet letter, encrypt it.
            # Find the index of the character in the alphabet.
            p = alphabet.index(char)
            # Apply the encryption formula: (a * p + b) mod m.
            c = (a * p + b) % m
            # Append the encrypted character to the ciphertext.
            ciphertext += alphabet[c]

        else:
            # If the character is not in the alphabet, keep it unchanged.
            ciphertext += char

    # Return the encrypted ciphertext.
    return ciphertext


# Define the plaintext and key components.
plaintext = input("[?] Enter text to encrypt: ")
A = 3
B = 10

# Call the affine_encrypt function with the specified parameters.
encrypted_text = affine_encryption(plaintext, A, B)

# Print the original plaintext, the key components, and the encrypted text.
print(f"[+] Plaintext: {plaintext}")
print(f"[+] Encrypted Text: {encrypted_text}")
