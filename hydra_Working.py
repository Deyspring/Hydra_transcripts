#!python
# 

import time
from selenium import webdriver
import manage_excel


# Accept user input and return a list of terms 
terms =[]
term = None

while term != 'done': 
	print('Enter "done" when done entering terms')
	term = input('Enter search term(s): ')
	terms.append(term)
