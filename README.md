#Unit testing

# 12/17 Well, I thought I was doing pretty well on this project until I saw this very reasonable list that I've made here. Anyways. Plugging along. 

### Ideas for tests

# X has a spreadsheet been created 
# Has the date/time been created and placed in column 
# Has the title been placed in column
# Has the phrase "search term" been created and placed in column
# Has an input been created for the search term. Has the search term been saved under a variable name, "GOI"
# Has a row been created or left empty under that 
# Has the title "gene of interest" been created and placed in the leftmost column (col1? ) at a certain row below the row before it? 

# Has the GOI been entered into the search box? 


https://selenium-python.readthedocs.io/navigating.html#filling-in-forms
Filling in the forms by entering in a keyword and activating the search button with a virtual click
<input type="text" name="keyword" id="keyword" value="" size="42" autocomplete="off" onkeyup="ajax_showOptions(this,'getDomainsByLetters',event)">

References: 
https://selenium-python.readthedocs.io/navigating.html#filling-in-forms

# Have the genes of interest been stripped and entered into a dictionary with the original ids? 
How do you select each item individually on that list and get the list of transcripts? 
Once the gene identifier is selected, how do you select the list of transcript names? 

## To find the individual transcripts##
Go to the Tracks descriptions page, uncheck all of the boxes on the left that are not concerned with the gene of interest. 
Go to developer tools and check networks tab then filter by XHR. 
Look on left for trackData.json and click on it to find the names and symbol numbers of the tracks you're interested in. 

#Is the transcript code stripped?  
	character code starting with t and ending before | (ie."t9735aep" from  Symbol:   t9735aep|92125)

# If there are no transcripts found, is "none" written in the column 

Is the transcript code listed next to the transcript name? (Column/row config to be determined)
 transcript      Juliano_aep   Juliano_aep2
                 t20369aep      None
                 t9735aep


#### 

Dependencies 

This module must be installed at the command line: openpyxl 

command syntax: pip install openpyxl for windows
				pip3 install openpyxl for Osx


GET ALL THE LINKS

Bleah. New plan. I absolutely can't use the google search method shown in Automate the boring stuff to fill in the text search box. I believe I'm looking at a form fill problem. I'm going to give 10 more min to seeing if I can use the google method and then start researching filling forms. Sigh. 


#### Using Selenium to fill forms 



table = soup.find_all('table')[0] # Select the table with the Gene Identity lin
                                  #This does not work because the TOI is nested inside a table

# This is harder than it seemed, there are nested tables with similar names and links with similar Id's 
# Below are methods and ideas to isolate the desired table cols and the links inside. 

#Example with lambdas, but the table I need to find has no id tag However the Form it was nested inside did have a unique identifier. I'm trying the Lambda example because it is more readable. I don't know what lambdas are though. 
#This does not find a nested table as far as I can tell. 


table = soup.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="Table1") 
rows = table.findAll(lambda tag: tag.name=='tr')


# Nested example 

table = soup.find('div',attrs={"class":"table-info"}) # This table had a class that could be identified
spans = table.findAll('span')

for span in spans:
    if span.text.lower() == 'branch':
        # Do your manipulation



#Ok, let's list any identifiers possible with nesting

<div class = "global content">
	<table border = "0">  # this is the third table on the page and only one with border 
		<tbody>
			<tr>
				<td valign = "top">
					<form method ="post" name = "checkboxform" onsubmit ="return redirectOutput(this)">. # This is a unique identifier. Yay! 
						<table border="0" class="styled" style='margin-left:0px">
							<tbody>
								<tr> -3rd down 
									<td>
										<a>   - a down the table until </tbody>


#############################################
GET THE BROWSER DRIVER RUNNING
##############################################

This has been a multiday affair to figure out. I wanted to use chrome as my browser, for no real good reason and was trying to get the suggested code from Automate the Boring stuff to work. It didn't. Here are the four lines I've been troubleshooting for two days. 

>>> from selenium import webdriver
>>> browser = webdriver.Firefox()
>>> type(browser)
<class 'selenium.webdriver.firefox.webdriver.WebDriver'>
>>> browser.get('http://inventwithpython.com')

Here's the solution: 
Install Homebrew  
https://www.saintlad.com/how-to-install-homebrew-on-mac/
Then install Chromedriver
https://www.kenst.com/2015/03/installing-chromedriver-on-mac-osx/

Then! When running this line
>>> browser = webdriver.Firefox()
Do not close the browser that appears. If you do, the following line won't work. 
browser.get('http://inventwithpython.com')

I noticed that a number of unique chrome browsers opened after playing with this command. I'm not sure if that's a good, bad or inconvienent thing. 


