# my Pets

myPets = ['eddy', 'karl', 'air-head', 'finn']
print('Enter a pet name:')
name = raw_input()
if name not in myPets:
	print('I do not have a pet named ' + name)
else:
	print(name + 'is my pet.')