

def save(text, text2):
    with open("atrained.txt", "a") as f:
        f.write(f"{text} | {text2.strip()} | no")

def save_as_question(text, text2):
    with open("atrained.txt", "a") as f:
        f.write(f"{text} | {text2.strip()} | yes")

def train():
    with open("auto_train.txt") as train_file:
        line_num = 0
        for line in train_file:
            split = line.split(" | ")
            line_num += 1
            if line.startswith("#"):
                print("comment dectected on line " + str(line_num))

            elif line.startswith(";"):
                split = line.split("; ")
                print("question dectected on line " + str(line_num))
                save_as_question(split[0], split[1])
            else:
                save(split[0], split[1])
train()