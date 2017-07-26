def isphoneNumber(text):
	if len(text) != 12:
		return False
	for i in range(0,3):
		if not text[i].isdecimal():
			return False
	if text[3] != '-':
		return False
	for i in range(4, 7):
		if not text[i].isdecimal():
			return False
	if text[7] != '-':
		return False
	for i in range(8,12):
		if not text [i].isdecimal():
			return False
	return True

	

	"""

	print('415-555-4242  is a phone number:')
	print(isphoneNumber('415-555-4242'))
	print('Moshi Moshi is a phone number:')
	print(isphoneNumber('Moshi Moshi'))

	"""

	message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
	for i in range(len(message)):
		chunk = message[i:i+12]
		if isphoneNumber(chunk):
			print('Phone number found: ' + chunk)
	print('Done')

	
