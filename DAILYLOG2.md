
The Daily log
-----------------
08/04/2020
I am being lazy and slow today. I haven't gotten much done, I haven't even done some yoga or a nice long walk. I haven't tried to stop myself from reading the news. Basically, I've eaten, had a call from the Job club and have done the GID group at 12:30. I didn't sleep well last night, but meh. I can overcome that to some degree. I'd really like caffeine now, but that's not going to happen. I'd like to see if I can get the hydra project to work with briefcase today. If I can, I'll shoot a message off to Callen and let her know that she should see something by the end of the week. 

Beeware tutorial finished. 
Time to make the Hydra project work with Beeware. 
0. Git everything
1. create project folder and activate virtual environment
2. Install briefcase in venv and bootstrap "briefcase new"
3. Check to see that new app is working with no modifications
4. Hard part: 
    Alter 'hydra_return_transcripts.py' file. a lot. 
    z. create window, column
    a. create terms.label widget 
    b. create terms input widget (form field) 
      - separate terms with commas? enter each one in one by one and press button each time? 
      - do last for now, add ability to load lots of terms at once later. 
    c. "done" button widget
    d. Add terms box and button widget to main method
    e. link other methods to button widget - this is called a handler method that is called whenever the button is pressed. 
    d. enter all these terms into appropriate method. 
    e. Does beeware work with multiple methods? find out. 

I think that's enough for today. If I finish it, the next thing will be the packaging and distribution tests. 


08/3/2020
Checked the news today, but it will be the last time. I need to reformat my computer today, I've been putting it off. 

Hours and hours and hours later, my Os has been reset to defaults. My new thumbdrive is pretty damn slow, even after I reformated it. This may be because of the USB adaptor, but that's just speculation. 

Also, I checked the news twice. Sigh. 

Alrighty, on to finishing the BeeWare tutorial. 


07/31/2020
Almost managed to not check the news today. Let's see if I can make this the only time. No Ann Friedman either. 
I'm having problems with my computer and will have to wipe it and reinstall everything. I really don't want to do this, so I'm putting it off until the weekend, probably after Python in the morning. 

I made great progress yesterday, I got everything working and managed to speed up the script. My code was starting up Firefox multiple times to get the links. Passing the browser variable to all the modules sped things up beautifully. Because the computer is foobared, I made a copy of the working code while I continue to optimize what I have and improve other bits to make the code more professional. 

07/30/2020
Oh yeah, I have to pay rent. My lungs hurt today, I've been having trouble breathing. I can't keep talking to Sally for 45+ daily. It's neat to talk with her, but we both need to get things done. 

I circled back around to the requirments and install packages. I need to track down why the script isn't finding the proper website and for the love of god, fix the length of time it takes to load up all the Json urls. 

Yay!!! It's working solidly. I have not written test cases for it, so I consider it to be fragile still. I'm going to see if I can save it to my Git repo and then I'll do the BeeWare tutorial to see if I can get this thing packaged up in a user friendly way. 

#For Mac
#homebrew == brew is not a package, it can't be installed easily  
#brew install geckodriver
# I installed geckodriver with brew, but this won't work for prepackaging. 


#There is an easy way to install Geckodriver:
#Install webdrivermanager with pip
#pip install webdrivermanager

#Install the driver for Firefox and Chrome
#webdrivermanager firefox chrome --linkpath /usr/local/bin

#Or install the driver only for Firefox
#webdrivermanager firefox --linkpath /usr/local/bin

#Or install the driver only for Chrome
#webdrivermanager chrome --linkpath /usr/local/bin


#Use this for PC 
#from selenium import webdriver
#from webdriver_manager.firefox import GeckoDriverManager


So, yay. The requirments.txt file is installing everything well and I might not need to use the additional_requirements.sh script. It's nice to know how to make a script file now though. 

This is the message I got when I ran the script: 
/Users/katherinedey/Pictures/Code/GitHub/Hydra_transcripts/addtional_requirements.sh 
Downloading WebDriver for browser: "firefox"
1835kb [00:00, 2051.50kb/s]                                                                                                                                                 
Symlink target /usr/local/bin/geckodriver already exists and will be overwritten.
Driver binary downloaded to: "/Users/katherinedey/Pictures/Code/GitHub/Hydra_transcripts/hyvenv/WebDriverManager/gecko/v0.27.0/geckodriver-v0.27.0-macos/geckodriver"
Symlink created: /usr/local/bin/geckodriver

So, genome_browser_links is badly constructed in that Firefox has to be loaded everytime a new link is needed. Firefox should be opened only once and the pages should be opened and closed after Firefox is loaded. I seem to recall having an issue with opening the browser pages correctly and that's why I left the function as it was. It needs to be fixed. This program is running so. slow. 



07/29/2020

So it's been a wild four months. I was furloughed, with no anticipation of getting rehired. Good, I didn't like that job and now I don't have to quit or get fired. 
I caught Corona, I'm pretty sure that I did. If it wasn't such a pain to get tested for antibodies, I'd do it to make sure. 

MEANWHILE, I discovered BeeWare. I'm hoping it will make the packaging process easier. Onward. 

Figure out what packages, etc. are required to run this program and put them into the requirements folder. Fix the 04/06 things. Get it to run, I moved the folder and everything broke. I deliberately deleted the virtual environment to see what requirements popped up that need to be installed. 

Did not get far today, just refamiliarizing myself with the code. I need to set up a pass around the url that can't be found. It is probably there, but something is causing it to not show up. I'm going to try and get everything working with some tests and then come back to the url problem

04/06 
Monday. 
I got the manage_xl script working. It's not as pretty as I'd like, but I'm getting tired of this project and just want to finish it now. 

Ask where to save exel files. 
format exel file to fit data. 
Make sure script is getting the correct information 

Batch file to get the thing installed quickly on Callen's end. I'll bundle it up and send it to Karen. 

04/03 

Huh. It's friday. I spent a little time on the manage_xl module problem. Using Zip to group the iterables together properly was the right answer, I just needed to put some conditionals in the script to let it know when to _not_ zip when there were one or fewer terms. The point of the zipping was to combine the terms, geneids and transcripts correctly, but that only works when all the iterables are lists and sets and not single word strings. 

It would be a good idea to roll back the manage_excel and create a function for the term header on the spreadsheet. 



03/31
Do. not. feel. ew..
Diareha, slightly warm, slight sore throat. Not enough soup. :P 
Still have a snese of smell though. 

The zip function is the source of the spreadsheet fill silliness. 
I'm trying to figure out how to loop things.... mh. Maybe I need to loop the iterables together first and then pass them out to the spreadsheet.

I also asked the slack about taking this project and bundling it in some way to make it easy to install and use. 


03/27
Hey today is Friday! Lookit that. 

Wasn't able to fix the spreadsheet bug yesterday. I'm pretty sure I fixed it before and the test of the module by itself was working. I'll test the module again, just in case and see if I can track this bug down. :P 

I researched packaging this up for easy installation and ran into a couple issues. 
Callen's using a Windows machine, I'm using a mac. That's the first of many issues, it looks like a difficult problem. 

I'll research UI for this program as well. It would be good to look into UI programming before packaging it up. I'm not sure if I can make it universal. It may make the most sense to turn it into a webtool. 


03/26
I've been losing track of the days. Four days. Yeah. 

XFormat spreadsheet 
XLabel terms, geneids and transcripts
XMake term label bold

XResearch headless running. 
it would be useful so the screen could be used for other things while the program was running. 
XHeadless running operational

XPrint something if the program isn't able to find something due to a slow loading issue. 

Bug: Enter items into spreadsheet properly, they are stretched out and letter by letter again

Research UI and installation packaging. 





03/22
Testing of multiple search terms today. 
If "done" and nothing else entered, exit the program 
Some formatting of spreadsheet. 
Headless running? Research this, it may mean running the program without visably opening up andy webpages. I'm not sure this is important, it might be useful for folks to see pages being opened and scraped. 
Packaging to be delivered research
UI research 

03/21 

I have worked on this code between now and 03/12, I just forgot to take notes. 
In one week we've gone from somewhat normal to "oh shit, we're all locked down and shouldn't be around people"

Todo:
xClose browser windows after the program is done, and ideally while the modules are running
Headless running, so no windows need to be opened to the eye
xFix how the transcripts are being entered into the spreadsheet
Test to see how well entering multiple search terms works. - it crashed when a null entry was put in, an entry with no results also crashed the program
If the search term isn't found, produce a not found message and continue

The program is roughly working, yay! 

Headless running, bug testing, and packaging it up to deliver. UI interface would be nice too. 




03/12 
Just a couple minutes before bed. :P 
I forgot to document the issues before going to bed. 


03/11
Made a lot of progress, the excel module is splitting the geneid into separate letters, I think I've fixed this. 

Biggest issue: the json stripper is stripping the transcripts completely wrong from the json file. I will have to write a little piece of code to deal with this. There are multiple transcripts in each json file that are duplictes of each other, so I'll have to write a script to compair any new stripped items to older items before appending them to a list. 

03/10
Today's todos: 
Fixed a bunch of things and program runs until end, saving a spreadsheet. 
  - Transcripts are not being collected and stripped properly, I'm getting duplicates of the same transcript for each geneid, which is incorrect. 
  - The program is opening multiple windows and not closing all of them. This needs to be addressed as I have a dozen open versions of Firefox on my desktop now. Some did close properly though, which is encouraging. 
  - When the spreadsheet is made, it saves the first letter of a geneid spread down rows and the numerals of the gene id in another set of rows. WTF? This spreadsheet was working, so it must be getting bad data. Let's see if fixing problem #2 fixes the spreadsheet. 

03/8 
Stuck on iterating over the json text object and extracting the transcripts. I'm not sure why I thought I had solved the problem earlier. The dictionary contains nested lists and the lists contain the same transcript numbers multiple times. I really thought there was a simple way to strip the transcripts out without having to do a comparison to previous items to see if they are the same. 


03/07 

Ok. Window switching modules. 

Lots of progress! Finally at the Json browser. I got stuck in an infinite loop, the while True loop got me. See if the find by element_s_ trick works again.  


03/06 

- fix genome browser links module
-Not sure how to handle the window switching issue between the modules
-Maybe I can pass a browser link and module?
-It may be easier to change the program into one big program instead of having modules, other than the excell module. 
- Yeah. Let's change it to one large program and just get the damn thing working maybe. 



03/03 

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
Nope. I can't figure it out. There seems to be an automatic way to get a list of webelements using the selenium "find_elements_by_xpath(result_link).text".  The keys seem to be the element_s_ command and the .text module, which doesn't seem to work with element_s_ but works fine with element. 



03/01 
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






