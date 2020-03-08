
The Daily log
-----------------
03/07 
Feeling a little better emotionally today, I did yoga for an hour, trama exercises and hung out with Lucas. His team was ranked second in the Robotics trials. I'm physically tired and feeling peckish. May get a banana before bed. 

Ok. Window switching modules. 


03/06 
No journaling in my regular journal. I'm not sure if I'm just exhausted by the effort, manic and not doing it, avoiding thinking about things(very possible) because of the anxiety. Anyways, having a super crappy week, not enjoying life and generally just trying to hang in there. 

So. 

- fix genome browser links module

-Not sure how to handle the window switching issue between the modules
-Maybe I can pass a browser link and module?
-It may be easier to change the program into one big program instead of having modules, other than the excell module. 
- Yeah. Let's change it to one large program and just get the damn thing working maybe. 



03/03 
Voted. Haunted by ruminatingthoughts about unexpected afternoon fete by Richard. I was late comimg back from lunch. I do not want to be thinking about work right now. I have little free time now and I don't want to spend it thinking about work!!!  Did feel more energetic this morning, but I'm not sure if that's because I accidentally took my thyroid med in the evening. Sometimes this helps me sleep deeper. I'm not sure if that was the case last night. Anyways, save this experiment for the weekend. 

Back to the work with element_s_ 
*Reminder, absolute xpaths are a super bad idea and you're using them. Change them to relative paths. 

As Mark Twain said" I did not have time to write a short letter, so I wrote a long one" 

The solution was super simple, fast and compact. I now have a tidy search_terms module

-Changed most absolute xpaths. 

Todo
- Genome browser links module. 
- should the search module return a browser? This seems like a bad idea and also maybe not possible. 
- it seems like it make more sense for the main program to open the browser and control things. 
- Let's look into that. 

03/02
Super depressed, had to suppress sobs most of the afternoon. Hopefully will feel better after a good night's sleep. 

Nope. I can't figure it out. There seems to be an automatic way to get a list of webelements using the selenium "find_elements_by_xpath(result_link).text".  The keys seem to be the element_s_ command and the .text module, which doesn't seem to work with element_s_ but works fine with element. 



03/01 
New month. I'm so depressed and a little manic. I forgot, seriously forgot, to take my meds on Thursday. I was mentally out of it all Friday and lost my purse. Luckily I found it. Saturday I bing watched "The Expanse". Today I'm going for a walk with KAren. I hope I feel better by Monday. 

hydra_ts_working.py is not working. I have a problem with ending the while True loop when it's finding links. It finds the link and then, for some odd reason, can't add the term to the list. I solved this problem before but can't remember how I did it. 
I thought it was a problem with loading, but now I'm not so sure. 


2/26 

Just a little work, maybe, tonight. 
Ah. I don't think I do have an infinite loop, the script is just taking a long time. 
A progress bar would be helpful here. :P 



2/25 
Tired today, need to go workout, eat out, etc. .
X make sure "done" is not added to terms list. 
X fixed keywordElem error, added browser opening code back to search_term module
X terms redundancy fixed

got search_terms and hydra_ts_Working to play nice, now they are crashing. I managed
to make an infinite loop somehow when I got an error that seemed to be related to speed of reloading. 
The geneome_browser_links module needs to be tested by itself. 


2/24

Important, remember to use "ig" as a test search term when prompted.
The term(terms) loop is in both the hydra_ts_working script and the search_term module. Fix this redundancy
line 
File "/Users/katherinedey/Documents/GitHub/Hydra_transcripts/search_term.py", line 20, in search_geneid
    keywordElem.send_keys(term)
UnboundLocalError: local variable 'keywordElem' referenced before assignment

2/23
Search terms portion complete, a list of terms is produced

2/22
Still dealing with grief, Pardi died. Things did not go well at python group, I don't think I'll be going back for awhile. 

2/19
Got manage_xl.py module mostly working.  Things to work on: 

Accept list of search terms. 
  - 50% done. Only accepts one term

GeneID_json link
   url = get_link_to_genome_browser(geneid) Get this to work. 

Excel module
    - Formatting can be improved in datetime presentation and spacing between each term.

2/9
Less sick, still hacking 

2/7 still really, really sick. May get job. 
Almost got manage_xl.py module working, got stuck on the term loop and making sure it saves with a new name and doesn't overwrite. 

2/4  
Bleah. Interview prep, weekend stuff, sick yesterday. Here I am and I feel like I've forgotten everything I did already. 

Ok. Made progress. I got create_excel.create_header() to work in hydra_ts_Working.py, but for some reason when I was working on add_data_xl in that module, the terminal said it could not find the openpyxl file. Also, fell asleep when writing rest of log. 

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
  - 50% done. Only accepts one term
  use the command line input function to accept search terms and place them in a list. 


 GeneID_json link
   url = get_link_to_genome_browser(geneid) Get this to work. 

5. Excel module
    - Done
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






