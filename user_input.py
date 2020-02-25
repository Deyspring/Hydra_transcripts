#!python
#A module that accepts terms from the command line and outputs a list of terms 

def user_input()
	terms =[]
	term = None

	while term != 'done': 
	
		print('Enter "done" when done entering terms')
		term = input('Enter search term(s): ')

	terms.append(term)

return terms
