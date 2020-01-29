
The Daily log
-----------------
1/28

I didn't finish the cleanup yesterday and I need to rename some files tomorrow. json_stripper2 im looking at you.  The main hydra_ts_Working file is working, although I need to check some things. I need to add the execel modules to the start and end. Otherwise progress was made today. I might have something to show to Callen on Thursday. The code feels rickety, badly named and awkward, but hey. It's my first real project and it is coming along nicely. 


1/27
Massive cleanup of files, I have enough of them that I wasn't sure where code I made went or was supposed to go. .. ANyways, it still needs more cleanup before I do any more programming. Also unit tests need to be done on the functions. Karen had a way to get the json files cleaned up that she wasn't able to share with me on Saturday. Onward

1/21 
More progress has been made on the unit tests. I've made two excel modules to create and then populate the spreadsheet. 
They are not yet complete and the unit tests are harder to write for these. I'm afraid I'm kinda fudging on them right now so I can get a somewhat working version of the Hydra code to show Callen this week. 

I can't figure out how to do a while loop that depends on the results of a try except to figure out. 

I banged out a lot of sketchy code today, just to get an idea of how it should all work. In retrospect, I should have sat down with a piece of paper to figure that out and then worked on the unit tests. Nothing works, so I didn't make any progress. 

1/18

I have made two working modules, the create_excel.py module that makes an excell spreadsheet with header(eventually it will have functions to add geneIds and transcripts to the created spreadsheet) The search_pfam.py module accepts one search term and returns one gene id. Both modules have unit_tests, but I'm having difficulty writing the test for the excell module as the output is all in an excel file. I am trying to write tests that enter bad data to get proper fails too, but I'm struggling with that as well. I can see why people say not to write code until you've written a unit test for it, they are a little frustrating to write. 

I'm kinda burnt on the unit testing of the above modules, and will return to them later. Meanwhile, I'm going to start on another module while I have the energy and then return to this tomorrow. I have to bike back home before it gets dark so I can walk pardi and feed her. 

Rough code outline and possible modules: 

1.Accept list of search terms. 
  #use the command line input function to accept search terms and place them in a list. 

2.Create spreadsheet header
   -90% done

3. Open browser portal and call search_term from search_pfam.py
  - 90% done'

3a. clip off geneID portion so it can be looped 
    this section is proving to be harder than it seemed to make a unit test for. I'm stuck for now. 

4. GeneID_json link
   - ok, this could go one of two ways. 
        - get one geneId at a time and then the related transcripts and put these in spreadsheet
        -The geneID is needed to get the JSon, which is different each time the browser is opened. 
        -The geneIDs will need to be used one at a time. 
        -I can still put them in a list for use.... thinking about it. 
        -for now lets do them one at a time
5. Get 

5. Update excel module
    - put gene id and then transcripts into spreadsheet. 



1/15 

Karen added two suggestions to my TODO list: 
-Make the code take a list of requested terms
-Make a GUI 

First thing today, clean up and organize the file folder, duplicate Homepage_Search and rename it to transcript_retrieve.py 
Identify possible modules 
Write some unit tests. 


1/14 I've given up on figuring out how to download the .bed file from the dropdown. At this point I feel the code necessary to figure out the javascript necessary to get it from the dropdown menu is more trouble than it's worth and will be prone to hard to track down bugs. I'm going to download the .json file and clean the very messy data, which is still just a text file. :P 

Done! Accomplished. 
TODO:  Turn JsonStripper.py into a class? Set up a loop to aquire all transcripts
TODO:  Change Homepage_search.py to not go to the third browser page and just generate a json. 
I suspect this will be faster than opening and waiting for the browser to load. 
TODO: Loop through all results generated to get each set of transcripts
TODO: Put gene identifier and transcripts into a spreadsheet. 
TODO: generate spreadsheet from scratch? Not sure this is necessary or even desirable. 
TODO: Write up unit tests. 

Problem: the json addy is identical for two gene identifiers that are the same except for the last four digits. Check the json file data for the results to see if indeed the results are the same. I'm not sure why they would be, but keep this in mind. 




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



############# GENERAL NOTES #################################

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

# This was harder than it seemed, there are nested tables with similar names and links with similar Id's. Xpaths were the only way to reach the desired elements. However, my xpaths are currently full paths as non-full paths didn't seem to work. 


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






