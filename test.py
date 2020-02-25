#test 

terms =[]
term = None

while term != 'done': 
	
	print('Enter "done" when done entering terms')
	term = input('Enter search term(s): ')

	try: 
		type(term) == str
	except: 
		print('Inccorect entry, try again')

	terms.append(term)

print(terms)

