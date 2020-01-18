import hydra_ts
import unittest

class TestResults(unittest.TestCase):

	from datetime import date

	arguments = ( 'Pfam Domains',
				  'Pfam domains in predicted Hydra proteins',
				  'https://research.nhgri.nih.gov/hydra/pfam/.html',
				   1
			    )

	value = PfamDomains_1.xls

	def create_excel(self):
		# Creates a new spreadsheet with header based on website and current date
		result = create_excel.create_header(arguments)
		self.assertEqual(value,result, "Should be title: " +value)

if __name__ == '__main__':
	unittest.main()