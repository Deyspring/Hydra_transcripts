import hydra_ts
import unittest

class TestResults(unittest.TestCase):

	from datetime import date
	known_values = 'PfamDomains_1.xls'
	 arguments = ('Pfam Domains',
	             'Pfam domains in predicted Hydra proteins',
				 'https://research.nhgri.nih.gov/hydra/pfam/.html',
				 1 
				)

	def create_excel(self):
		# Creates a new spreadsheet with header based on website and current date
		result = create_excel.create_header(arguments)
		datestamp = (date.today()).strftime("%b/%d/%Y")
		file_wb = ('PfamDomains_1.xls')
		wb = openpyxl.load_workbook('PfamDomains_1.xls')
		sheet = wb['Sheet1']
		file_title = sheet['A1'].value
		file_subtitle = sheet['A2']
		file_web_address = sheet['A3']
		file_datestamp = sheet['A5']

		self.assertEqual(wb,result, "Should be spreadsheet: " +filename)
		self.assertEqual(file_title,result, "Should be title: " +title)
		self.assertEqual(file_subtitle,result, "Should be title: " +subtitle)
		self.assertEqual(file_webaddress,result, "Should be title: " +file_web_address)
		self.assertEqual(file_datestamp,result, "Should be title: " +datestamp)


if __name__ == '__main__':
	unittest.main()