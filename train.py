import time
def save(text, text2, q = "no"):
    with open("data.txt", "a") as f:
        f.write(f"\n{text} | {text2} | {q}\n")

#print("""
#""") i forgot what i put here lol
#time.sleep(5)
while True:
	text = input("user input>")
	text2 = input("bot output>")
	tmp = False
	while tmp is False:
		is_q = input("Will the user input be a question? y/n\n")
		if "y" in is_q.lower():
			tmp = True

			print(f"{text2} will be a response to {text} and it will be a question")
			save(text, text2, "yes")

		if "n" in is_q.lower():
			tmp = True

			print(f"{text2} will be a response to {text} but it will not be a question")
			save(text, text2, "no")