from difflib import SequenceMatcher
import util
from collections import Counter
from util import temp, get_temp
count = Counter()
count["is_first_try"] = 0

def get_response(text, question):
    if question is True:
        try:
            q_get_response(text)
        except:
            _get_response(text, False)
    else:
        _get_response(text, False)


def _get_response(text, question):
    try:
        nothing_found = False
        text = util.strip_and_lower(text)
        with open("data.txt", "r") as f:
            dumb = False
            for line in f:
                split = line.split(" | ")
                if line != "":
                    if str(SequenceMatcher(None, text, split[0]).ratio()) > '0.5': # prints the 2nd half if it matches the 1st
                        print("bot>" + split[1])
                        util.log(f"\n\nUser input -> {text}\nInput matched -> {split[0]}\nselected -> {split[1]} [with a a confidence of {str(SequenceMatcher(None, text, split[0]).ratio())}]\nis a question -> {split[2]}\n")
                        last_bot_input = split[1]
                        count["is_first_try"] += 1
                        temp(f"{split[1]}")
                        if util.already_exists(text) is False:
                            with open("data.txt", "a") as savedata:
                                if text.endswith("?"):
                                    savedata.write(f"\n{text} | {split[1]} | yes")
                                else:
                                    savedata.write(f"\n{text} | {split[1]} | no")
                                savedata.close()
                            nothing_found = True
                        return f.close()
        if nothing_found is False:
            print("I dont quite understand that")
            temp_log = f"The user input \"{text}\" but nothing came up"
            if str(count["is_first_try"]) != '0':
                temp_log += ", it is not first try"
                get_last_bot_output = get_temp()
                write_non_found = f"\n{text} | {get_last_bot_output}"
                if text.endswith("?"):
                    temp_log += " saving as a question"
                    write_non_found += " | yes"
                else:
                    temp_log += " not saving as a question"
                    write_non_found += " | no"
                with open("data.txt", "a") as f:
                    temp_log += f" writing this to the data file -> {write_non_found}"
                    f.write(write_non_found)
                    f.close()
            util.log(temp_log)

    except Exception as e:
        print("ERR " + str(e))


def q_get_response(text):
    text = util.strip_and_lower(text)
    nothing_found = False
    with open("data.txt", "r") as f:
        for line in f:
            split = line.split(" | ")
            if str(SequenceMatcher(None, text, split[0]).ratio()) > '0.5':
                if split[2] == 'yes': # i had a try/except but someone said that was cancerous so enjoy your errors when it throws index errors
                    nothing_found = True
                    util.log(f"\n\nUser input -> {text}\nInput matched {split[0]} ->\nselected -> {split[1]} [with a a confidence of {str(SequenceMatcher(None, text, split[0]).ratio())}]\nis a question -> {split[2]}\n")
                    return print(f"bot> {split[1]}")

    if nothing_found is False:
        util.log(f"User input \"{text}\" and was shown as a question, but nothing showed up, searching normally\n")
        _get_response(text)