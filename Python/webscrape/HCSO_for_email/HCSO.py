import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import re

url = 'http://apps.hcso.org/PropertySale.aspx'

#needed header to soppf browser
hdr = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'en-US,en;q=0.9',
    'Host':'apps.hcso.org',
    'Origin':'http://apps.hcso.org',
    'Referer':'http://apps.hcso.org/PropertySale.aspx',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
}

#1st page pull,
req = urllib.request.Request(url,headers=hdr) # includes urls and headers
response =urllib.request.urlopen(req)
f = response.read()

#parse page
soup_dummy = BeautifulSoup(f, 'html.parser')


# parse and retrieve needed form values
viewstate = soup_dummy.select("#__VIEWSTATE")[0]['value']
viewstategen = soup_dummy.select("#__VIEWSTATEGENERATOR")[0]['value']
viewValid = soup_dummy.select("#__EVENTVALIDATION")[0]['value']
viewTSM= soup_dummy.select("#ToolkitScriptManager1_TSM")[0]['value']


# form data to simulate clicking on upcomming forclosure button
formData = (
    ('__VIEWSTATE', viewstate),
    ('__VIEWSTATEGENERATOR', viewstategen),
    ('__EVENTTARGET', 'btnCurrent'),
    ('ToolkitScriptManager1_TSM', viewTSM),
    ('__EVENTVALIDATION', viewValid)
)

# 2nd HTTP request with form data to simulate clicking on upcomming forclosure button
data = urllib.parse.urlencode(formData)
data = data.encode('ascii')  # data should be bytes
req = urllib.request.Request(url, data, headers=hdr)
with urllib.request.urlopen(req) as response:
    the_page = response.read()

# parse page to get form data 
soup = BeautifulSoup(the_page, 'html.parser')

#re-retrive form fields incase they changed
viewstate = soup.select("#__VIEWSTATE")[0]['value']
viewstategen = soup.select("#__VIEWSTATEGENERATOR")[0]['value']
viewValid = soup.select("#__EVENTVALIDATION")[0]['value']

# find value for 3 date choice and update form data
Foreclosure_dates = soup.find_all('ul') #use soup to find tags that match date containing tags
Foreclosure_date = Foreclosure_dates[8].find_all('li')[3].text.strip() #item 8 with tage li and item 3 to text and striped
Foreclosure_ch = re.findall(r'[^/]+(?://[^/]*)*', Foreclosure_date) #use regex to pick only what is between ie 2/34/90
date = Foreclosure_ch[0]+"%2F"+Foreclosure_ch[1]+"%2F"+Foreclosure_ch[2] #join date in format need for forms
eventag = {"type":1,"index":3,"text":"","value":""} #insert date into form field value
ddlDate = {"enabled":"","logEntries":[],"selectedIndex":3,"selectedText":"","selectedValue":""}#insert date into form field value
eventag['text'] = date
ddlDate['selectedText'] = date
ddlDate['enabled'] = 'true'

# form data with fields need to simulate picking date in upcomming forclosure drop down
formData = (
    ('__VIEWSTATE', viewstate),
    ('__VIEWSTATEGENERATOR', viewstategen),
    ('__EVENTTARGET', 'ddlDate'),
    ('__EVENTARGUMENT', eventag),
    ('ToolkitScriptManager1_TSM', viewTSM),
    ('__EVENTVALIDATION', viewValid),
    ('ddlDate_ClientState',ddlDate)
)

# 3rd HTTP request with form data to simulate picking date in upcomming forclosure drop down
data = urllib.parse.urlencode(formData)
data = data.encode('ascii')  # data should be bytes
req = urllib.request.Request(url, data, headers=hdr)
with urllib.request.urlopen(req) as response:
    the_page = response.read()

# parse page to get form data
soup = BeautifulSoup(the_page, 'html.parser')

#re-retrive form fields incase they changed
viewstate = soup.select("#__VIEWSTATE")[0]['value']
viewstategen = soup.select("#__VIEWSTATEGENERATOR")[0]['value']
viewValid = soup.select("#__EVENTVALIDATION")[0]['value']

# formdata need to simulate go button click
formData = (
    ('__VIEWSTATE', viewstate),
    ('__VIEWSTATEGENERATOR', viewstategen),
    ('btnGo','GO'),
    ('__EVENTTARGET','btnGo_ClientState' ),
    ('ToolkitScriptManager1_TSM', viewTSM),
    ('__EVENTVALIDATION', viewValid),
    ('ddlDate_ClientState','')
)

# 4th HTTP request with form data to simulate go button click
data_fin = urllib.parse.urlencode(formData)
data_fin = data_fin.encode('ascii')  # data should be bytes
req_fin = urllib.request.Request(url, data_fin, headers=hdr)

with urllib.request.urlopen(req_fin) as response:
    the_page_fin = response.read()

# parse page to get form data
soup_fin = BeautifulSoup(the_page_fin, 'html.parser')

#find table rows with date
listings = soup_fin.findAll("tr")

#use first recored as headers for CSV field
heading = re.findall(r'col">(.*?)<\/th>',str(listings[0]))
# ['Case NO', 'Plaintiff', 'Defendant', 'Address', 'Atty Name', 'Atty Phone', 'Appraisal ', 'MIn Bid', 'Township', 'WD', 'Sale Date']

headers_csv = list()
for head in heading:
    headers_csv.append(head)

#regex expression for picking values
regex = r'<td>(.*?)<\/td>'

for x in range(1, len(listings)): #loop for length of listings, starting from 1 until len
    row = list() #create empty list
    heading_x = re.findall(regex,str(listings[x]))
    for i in [a for a in range(len(heading_x)) if a != 9]: #loop skipping item 9
        row.append(heading_x[i]) #add to list
    print(row)

#file process
filename = "HCSO-complete.csv"
f = open(filename,"w")
headers_csv = heading[1],

f.write(headers)



