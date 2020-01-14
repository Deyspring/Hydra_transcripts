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


############   To find the individual transcripts using API. ############

-Go to the Tracks descriptions page, Check Juliano-aepLRv2. Uncheck everything else. 

-Go to developer tools and check networks tab then filter by XHR. Refresh the page to see the json info
-Look on left for trackData.json and click on it to find the names and symbol numbers of the tracks you're interested in. 

-Click on Headers to find the Request URL 

This is the request url, which will produce different data every time. 
https://research.nhgri.nih.gov/hydra/jbrowse/data/tracks/aepLRv2_splign/Sc4wPfr_1127.1/trackData.json

-create a line to grab every line in the json file of the format "gene.t38613aep|23824"
- strip off the quotes and the gene. parts. 
- This is your transcript type t9735aep|92125
- There may be duplicate gene mentions, so check your database. 

# If there are no transcripts found, is "none" written in the column 

Is the transcript code listed next to the transcript name? (Column/row config to be determined)
 transcript      Juliano_aep   Juliano_aep2
                 t20369aep      None
                 t9735aep

Reference tutorial
http://www.gregreda.com/2015/02/15/web-scraping-finding-the-api/

#### 


https://selenium-python.readthedocs.io/navigating.html#filling-in-forms
Filling in the forms by entering in a keyword and activating the search button with a virtual click
<input type="text" name="keyword" id="keyword" value="" size="42" autocomplete="off" onkeyup="ajax_showOptions(this,'getDomainsByLetters',event)">

References: 
https://selenium-python.readthedocs.io/navigating.html#filling-in-forms


######################################
Spreadsheet module

This module must be installed at the command line: openpyxl for spreadsheet file manipulations

command syntax: pip install openpyxl for windows
				pip3 install openpyxl for Osx
#################################



#### Using Selenium to fill forms 

table = soup.find_all('table')[0] # Select the table with the Gene Identity lin
                                  #This does not work because the TOI is nested inside a table
                                  # Use Xpath instead

# This is harder than it seemed, there are nested tables with similar names and links with similar Id's 
# Below are methods and ideas to isolate the desired table cols and the links inside. 

#Example with lambdas, but the table I need to find has no id tag However the Form it was nested inside did have a unique identifier. I'm trying the Lambda example because it is more readable. I don't know what lambdas are though. 
#This does not find a nested table as far as I can tell. 




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


The Daily log
-----------------
1/14 I've given up on figuring out how to download the .bed file from the dropdown. At this point I feel the code necessary to figure out the javascript necessary to get it from the dropdown menu is more trouble than it's worth and will be prone to hard to track down bugs. I'm going to download the .json file and clean the very messy data, which is still just a text file. :P 


1/10?
This code is pretty simple right now, but after the text is entered and submitted, no search items return 
Something happens, the browser refreshes, but nothing else. 
# Now I'm wondering about how the text is entered and the autocomplete java stuff. 
# And also if the search is being blocked by some sort of automatic script sensor

#I'm going to try the Firefox driver and see if that makes any difference - nope!
# After a bit more careful peering at the html, I noticed the onkeyup option and did 
# research I wish I'd done sooner. It was triggering the execution of some javascript. 
# Solution below. 
#Fuck yeah! sucess!!! I used the click() method and pinpointed the elements using xpath
#The element's xpaths can be copied in the developer window after selecting them. 

#next, sectecting one gene id link and putting that link name in a spreadsheet. make this a separate method

#After doing some reading I realized that my xpaths are absolute and should be changed to relative. 
#I'm trying to figure out the best way to select the gene id name, which does not have a tag or id attached to it. 
#This may require a chained? xpath. Xpaths are going to be my main way of finding elements on this website. :P 
# First, change absolute links to relative ones. 
#Ok, I tried to change the absolute links to relative ones and that did not work. The relative link would not allow a keyword to be entered into the search bar, for instance. 

#An unsatisfying day of coding, however while cleaning up my project space I realized that I'd entirely forgotten about using an API to get the table data and gene fragments. Tomorrow's quest then. 

1/8/2020

My notes are not too organized, but in my defense, I thought this project would take a week. 
I found the API, but am not sure how to utilize it yet. 
I believe I need to write a little script to uncheck and check some boxes.
There is a possiblity that I can download all the transcripts from a little box I found up to the right. I would not need to access the API then and it might be easier to clean the data. 

Yep. The Bed file provides a nice little list of all the transcripts. Tomorrow checkbox file scripts. 

https://research.nhgri.nih.gov/hydra/jbrowse/display_jbrowse.cgi?loc=Sc4wPfr_1127.1%3A428974..461132&tracks=augustus%2Cscaffold%2CaepLRv2_splign&highlight=

	Sc4wPfr_708.g2567.t1


https://research.nhgri.nih.gov/hydra/jbrowse/display_jbrowse.cgi?loc=Sc4wPfr_708%3A1..47088&tracks=augustus%2Cscaffold%2CaepLRv2_splign&highlight=

<a href="/hydra/jbrowse/display_jbrowse.cgi?loc=Sc4wPfr_708%3A179350..226463&amp;tracks=augustus,scaffold&amp;highlight=" target="_blank">View Gene in Genome Browser</a>

https://research.nhgri.nih.gov/hydra/jbrowse/display_jbrowse.cgi?loc=Sc4wPfr_708%3A179345..226458&tracks=augustus%2Cscaffold&highlight=

https://research.nhgri.nih.gov/hydra/jbrowse/display_jbrowse.cgi?loc=Sc4wPfr_708%3A179345..226458&tracks=augustus%2Cscaffold&highlight=


from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()
driver.get('url')

select = Select(driver.find_element_by_id('fruits01'))

# select by visible text
select.select_by_visible_text('Banana')

# select by value 
select.select_by_value('1')
