from difflib import SequenceMatcher

from collections import Counter

from main import logic

import time

count = Counter()
count["is_first_try"] = 0

def get_response(text, question, ratio = 0.5, adapter = "compare"):
	"""
	Get a response to input (text)
	Ratio is the confidence level needed for the bot to return a response 1.0 - 0.1
	Question will mark it as a question and it will try to find a answer (deprecated)
	Adapter:
		Based on the adapter you choose it will highly affect the bot
		Adapters:
			Compare:
				Grabs the first response that has a high confidence
			Best Match:
				Grabs all responses that have high confidence and selects the one with the highest"""
	
	return _get_response(text, adapter, ratio)


def _get_response(text, adapter, ratio):
	"""
	Feeds the input (text) into the bot
	Adapter:
		See 'get_response' so see about adapters"""
	start = time.monotonic()
	nothing_found = False
	response = {"response": "None", "time": "None", "confidence": "None"}
	start = time.monotonic()
	with open("stored/data.txt", "r", encoding="utf-8") as f:
		dumb = False
		lines = []
		for line in f:
			if line != "":
				lines.append(line)
		try_getting_response = logic.adapter(adapter, text, lines, ratio)
		if try_getting_response is not None:
			response["response"] = try_getting_response["output"]
			response["confidence"] = try_getting_response["confidence"]
			nothing_found = True
			
	if nothing_found is False:
		response["response"] = "I dont quite understand that"
		response["confidence"] = "0"
	end = (time.monotonic() - start) * 1000
	response["time"] = end
	return response



