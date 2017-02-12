SPECIAL_CHARACTERS = {
	'.': '<STOP>',
	',': '<COMMA>',
}
START_OF_FILE = '<SOF>'
END_OF_FILE = '<EOF>'

def tokenize(text):
	tokens = [START_OF_FILE]

	current_token = ''
	for c in text:
		if c in SPECIAL_CHARACTERS:
			tokens.append(current_token)
			tokens.append(SPECIAL_CHARACTERS[c])
			current_token = ''
		elif c == ' ':
			tokens.append(current_token)
			current_token = ''
		else:
			current_token += c

	tokens.append(END_OF_FILE)

	return tokens
