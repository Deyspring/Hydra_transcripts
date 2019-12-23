#Unit testing


### Ideas for tests

# has a spreadsheet been created
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

# Have the genes of interest been stripped and entered into a dictionar with the original ids? 
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






