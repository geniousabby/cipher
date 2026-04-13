
"""
Adding to #1, write a function called "send_messages()" that prints each text message
and MOVES each message to a new list called "sent_messages" as it's printed.
After calling the function, print both of your lists to make sure the messages were moved correctly
(there should be nothing left in the original list after it has been moved).

"""

# list to store messages
messages = ["Saanvi is the best.", "Saanvi is EVIL!", "Who is Saanvi?"]


sent_messages = []


# Send messages
def send_messages():
    """
    stores messages to send
    
    """
    sent_messages.append(messages.pop(0))
    sent_messages.append(messages.pop(1))
    sent_messages.append(messages.pop(2))


def main():
    """
    Main function that calls the other functions.

    """

    # Run send_messages function
    print(messages)
    print(sent_messages)


if __name__ == "__main__":
    main()
