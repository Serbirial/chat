print("""
Commands:
    <quit>
    <time>
    <math>
    <clean_start>""")
from difflib import SequenceMatcher
import util
from collections import Counter
from main.user import *
import sys
import datetime
from main.commands import *


def redHammingMod(s1, s2):
    s1 = s1 + ' ' * (len(s2) - len(s1))
    s2 = s2 + ' ' * (len(s1) - len(s2))
    distance = sum(i == j for i, j in zip(s1, s2))
    norm_distance = distance / float(len(s1))
    return norm_distance

def bot(user_input, adapter = "get_best_match"):
    """Takes the user inpurt and gives it to the bot, also checks for any commands"""
    last_user_input = str(user_input)
    command = check(last_user_input)
    if command is not None:
        return command
    #if last_user_input.endswith("?"):
    #    return get_response(last_user_input, True, adapter)
    #else:
    return get_response(text=last_user_input, question=False, ratio=0.4, adapter=adapter)

if __name__ == "__main__":
    h = True
    while True:
        while h is True:
            ad = input("what adapter do you want>")
            if ad.lower() != "compare":
                if ad.lower() != "get_best_match":
                    print("Invalid")
                else:
                    h = False
            else:
                h = False
        inp = input("\nyou>")
        response = bot(inp, ad)
        print("bot>", str(response["response"]))
        print("confidence -> ", str(response["confidence"]))
        print("time -> ", str(response["time"]))


# ratio = SequenceMatcher(None, a, b).ratio()



