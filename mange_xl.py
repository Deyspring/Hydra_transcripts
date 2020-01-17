# python!
# Create_excel makes an excel file with a title based on a website and the date. 

import openpyxl
import time

title = 'Pfam Domains'
subtitle = 'Pfam domains in predicted Hydra proteins'

def create_xl(title,subtitle):

#Create an excel file
wb = openpyxl.load_workbook('hydra.xlsx')
sheet = wb.get_sheet_by_name('Sheet1') #top sheet



wb.save('UpdateHydra.xlsx')
