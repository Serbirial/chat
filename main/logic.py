import string
from difflib import SequenceMatcher
from string import ascii_letters, punctuation, whitespace
import util


def already_exists(to_check):
	"""
	Checks the file to see if the text or response and input combo is already there
	To check:
		The text to check for in the file"""
	try:
		with open("stored/data.txt", "r") as f:
			for line in f:
				if line != "":
					split = line.split(" | ")
					if split[0] == to_check or split[1] == to_check:
						return True
					else:
						return False
	except:
		return True

def compare(user_input, text_to_search, ratio = 0.6):
	"""
	Compare {user_input} to {text_to_search}
	Ratio is the confidence needed to pass and give True
	Picks the first response"""
	responses = []
	for line in text_to_search:
		split = line.split(" | ")
		responses.append(split[0] + ' | ' + split[1])
	for word in responses:
		split = word.split(" | ")
		if str(SequenceMatcher(None, user_input, split[0]).ratio()) > f'{ratio}':
			util.log(f"Used '{split[1]}' as a response to '{user_input}' with a confidence of {str(SequenceMatcher(None, user_input, split[0]).ratio())}")
			return split[1]

def compare_old(user_input, text_to_search, ratio = 0.6):
	if str(SequenceMatcher(None, user_input, text_to_search).ratio()) > f'{ratio}':
		return True
	else:
		return False

def get_best_match(user_input, text_to_search, ratio = 0.6):
	"""
	Gets the best match out of multiple responses
	User input:
		The users input, this should be a string
	Text to search:
		The text to search, this should be a array
	Ratio:
		The ratio that confidence should be near to continue"""
	responses = []
	response = {"output": "None", "confidence": "None"}
	for word in text_to_search:
		split = word.split(" | ")
		if str(SequenceMatcher(None, split[0], user_input).ratio()) > str(ratio):
			responses.append(split[0] + ' | ' + split[1]) # add each response to an array if it matches the conf ratio

	last_res = []
	didnt_find = True
	for res in responses:
		split = res.split(" | ")
		conf = compare_old(user_input, split[0], ratio + 0.3)
		if conf is True:
			if conf != "":
				util.log(f"Selected \"{split[1]}\" as a response with a confidence higher than {ratio+0.3}")
				response["output"] = split[1] # returns the one that matches the given ratio + 0.3
				didnt_find = False
	if didnt_find is True:
		for res in responses:
			split = res.split(" | ")
			conf = compare_old(user_input, split[0], ratio + 0.2)
			if conf is True:
				if conf != "":
					util.log(f"Selected \"{split[1]}\" as a response with a confidence higher than {ratio+0.2} (second try")
					response["output"] = split[1] # returns the one that matches the given ratio + 0.2
					didnt_find = False
	if didnt_find is True:
		return None 
		util.log(f"Found no response, passing")
		#return "Sorry, i dont understand that"
	response["confidence"] = str(SequenceMatcher(None, split[0], user_input).ratio())
	return response

def adapter(adapter_chosen, user_input, line, ratio = 0.5):
	"""
	Finds the adapter and then uses it with the given input, line and ratio
	Adapters:
		Compare:
			Grabs the first response that has a high confidence
		Best Match:
			Grabs all responses that have high confidence and selects the one with the highest"""
	adapters = ["compare", "get_best_match"]
	adapters_func = {"compare": compare, "get_best_match": get_best_match}
	for option in adapters:
		if option == adapter_chosen:
			return adapters_func[adapter_chosen](user_input, line, ratio)