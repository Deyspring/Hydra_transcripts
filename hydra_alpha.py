#!python

# Hydra code - alpha version
# This code takes search terms and returns a spreadsheet populated with geneIds and their transcripts


import time
from selenium import webdriver
import search_pfam 
import create_excel
import JsonStripper


#Create a new excel document
#Should these be default, or should users be prompted to enter terms each time? 
title = 'Pfam Domains'
subtitle = 'Pfam domains in predicted Hydra proteins'
web_address = 'https://research.nhgri.nih.gov/hydra/pfam/'
#TODO make sure to make a new spreadsheet every time
number = '1'
create_excel.create_header(title, subtitle, web_address, number)

#Open Firefox web browser
browser = webdriver.Firefox()
browser.get('https://research.nhgri.nih.gov/hydra/pfam/')

###Home page: window_first
window_first = browser.window_handles[0] # Store this variable before clicking any links
input_string = input('Enter "ig" to test script: ') #TODO: make it possible to enter a list of terms

gene_ids = search_term(input_string)

for gene_id in gene_ids: 
	transcripts = transcripts_from_Json(gene_id)
	update_excel(gene_id, transcripts)

#TODO close browser










