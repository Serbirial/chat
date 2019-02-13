import sqlite3


def save(text, text2):
    with open("output_from_convert.txt", "a") as f:
        f.write(f"{text} | {text2.strip()} | no\n")



def sql_to_txt(chatterbot_chat_file):
	con = sqlite3.connect(chatterbot_chat_file)
	cur = con.cursor() # handles requests made to the database
	for row in cur.execute('select text, statement_text from response'):
			save(row[0], row[1])
			print("text: " +  row[0])
			print("statement_text: " + row[1])