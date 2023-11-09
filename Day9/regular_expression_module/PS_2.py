import re


def check_greeting(sentence):
    pattern = r"^Hello"

    if re.search(pattern,sentence):
        print("Ok")
    else:
        print("You didn't say hello")
