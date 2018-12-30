import string

def strip_and_lower(string_input):
	"""
	Will remove punctuation from an inputted string and
	return the lowercase version of that parsed string.
	Any innuendo is unintentional.
	"""
	#table = string_input.maketrans(
	#    {symbol: None for symbol in string.punctuation}
	#    )
	#string_wo_punc = string_input.translate(table)
	return string_input.lower() # was causing problems

def temp(stuff):
	with open("tmp.txt", "w") as f:
		f.write(f"{stuff}")
		f.close()

def get_temp():
	with open("tmp.txt", "r") as f:
		for line in f:
			if line != '':
				return line
				f.close()

def log(text):
	with open("other/logs.txt", "a+") as f:
		f.write(f"{text}")
		f.close()

def already_exists(to_check):
	try:
		with open("data.txt", "r") as f:
			for line in f:
				if line != "":
					split = line.split(" | ")
					if split[0] == to_check or split[1] == to_check:
						return True
					else:
						return False
	except:
		return True