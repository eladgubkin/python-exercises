x = 1
while x <= 5:
	message = input('Enter your message')
	result = ''

	for letter in message:
		if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
			letter = letter + 'b' + letter
			result = result + letter

		else:
			result = result + letter

	print(x, ")", result)
	x = x + 1
