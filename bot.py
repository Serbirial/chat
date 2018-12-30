from difflib import SequenceMatcher
import util
from collections import Counter
from main.user import *


def redHammingMod(s1, s2):
    s1 = s1 + ' ' * (len(s2) - len(s1))
    s2 = s2 + ' ' * (len(s1) - len(s2))
    distance = sum(i == j for i, j in zip(s1, s2))
    norm_distance = distance / float(len(s1))
    return norm_distance

while True:
    inp = input("\nyou>")
    last_user_input = str(inp)
    if inp.endswith("?"):
        get_response(inp, True)
    else:
        get_response(inp, False)


# ratio = SequenceMatcher(None, a, b).ratio()



