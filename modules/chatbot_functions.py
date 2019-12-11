# This class contains the chatbot's functions
from modules.responses import *

def grookey_says(text):
    """When printing chatbot responses, prefixes those responses with the chatbot's name."""
    message = "Grookey: " + text
    print(message)

def parse_input(u_input):
    """Changes input to all lower case and removes any non-alphabetical or non-whitespace characters"""
    u_input = str(u_input).lower()
    parsed_input = ''
    for c in u_input:
        if c in acceptable_characters:
            parsed_input += c
    return parsed_input

def start_bot(user_input):
    """Input analysis function specialized to look for the strings to start the chatbot"""
    user_input = user_input.split(' ')
    for word in user_input:
        if word not in greetings:
            return False
    grookey_says(common_replies['start'])
    return True

def end_bot(user_input):
    """Input analysis function specialized to look for the strings to stop the chatbot"""
    user_input = user_input.split()
    if (bot_name not in user_input):
        return False
    for word in user_input:
        if word not in goodbyes:
            return False
    grookey_says(common_replies['end'])
    return True


def give_answer(question):
    """General input analysis function that checks user input for any matches to the chatbot's response library"""
    for ape in ape_subjects:
        if ape in question:
            grookey_says(conversation_topics[ape])
            return False
    if question in conversation_topics:
        grookey_says(conversation_topics[question])
    else:
        grookey_says(common_replies["no answer"])
    return False


def input_loop():
    """Creates a loop that allows the user to repeatedly enter input until the chatbot is stopped"""
    begin = False
    grookey_says(common_replies['onrun'])
    while (True):
        u_input = input("You: ")
        u_input = parse_input(u_input)
        if (end_bot(u_input) == True):
            break
        elif (begin == True and start_bot(u_input) == False):
            give_answer(u_input)
        elif (begin == False):
            begin = start_bot(u_input)

# References
# https://stackoverflow.com/questions/16060899/alphabet-range-in-python
