import os
import random

print("\033[1;32m")  # Set color to green
print("HELLO! Welcome to our Holiday messages generator!")
print("\033[0m")  # Reset color


def generate_message():
    holiday = input("What holiday do you want? ")
    messages = messages_file(holiday)

    if messages:
        name_choice = input("Do you wish to add a name to your message? ")
        if name_choice.lower() == "yes":
            name = input("What name? ")
            message = random.choice(messages)
            formatted_message = message.format(name)
            print(formatted_message) 
        else:
            message = random.choice(messages)
            message_noname = message.replace("{}","")
            print(message_noname)
    else:
        print("\033[1;31m Sorry, we dont have messages fot that holliday\033[0m")

def messages_file(holiday):
    filename = f"{holiday.lower()}.txt"
    messages = []

    if os.path.exists(filename):
        file = open(filename, 'r')
        messages = file.readlines()
        file.close()
    return messages


generate_message()