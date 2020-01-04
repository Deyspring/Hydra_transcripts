from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://research.nhgri.nih.gov/hydra/pfam/')
try:
    elem = browser.find_element_by_id('keyword')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')