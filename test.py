from difflib import SequenceMatcher
import util
from collections import Counter
from util import temp, get_temp
from main import logic


responses = []
nothing_found = False
with open("stored/data.txt", "r") as f:
    for line in f:
        responses.append(line)
print(logic.get_best_match("hello", responses))
