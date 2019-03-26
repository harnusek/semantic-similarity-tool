import re

def tokenize(sent):
	return re.split('; |, |\*|\n',sent)
