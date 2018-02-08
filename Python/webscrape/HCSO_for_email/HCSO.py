import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import re

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.17 (KHTML, like Gecko)  Chrome/24.0.1312.57 Safari/537.17',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'
}


class MyOpener(urllib.request.FancyURLopener):
    version = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.57 Safari/537.17'


myopener = MyOpener()
url = 'http://apps.hcso.org/PropertySale.aspx'
# first HTTP request without form data
f = myopener.open(url)
soup_dummy = BeautifulSoup(f, 'html.parser')
# parse and retrieve two vital form values
viewstate = soup_dummy.select("#__VIEWSTATE")[0]['value']
viewstategen = soup_dummy.select("#__VIEWSTATEGENERATOR")[0]['value']
viewValid = soup_dummy.select("#__EVENTVALIDATION")[0]['value']
viewTSM= soup_dummy.select("#ToolkitScriptManager1_TSM")[0]['value']


# search for the string 'input' to find the form data
formData = (
    ('__VIEWSTATE', viewstate),
    ('__VIEWSTATEGENERATOR', viewstategen),
    ('__EVENTTARGET', 'btnCurrent'),
    ('ToolkitScriptManager1_TSM', viewTSM),
    ('__EVENTVALIDATION', viewValid)
)


# second HTTP request with form data
data = urllib.parse.urlencode(formData)
data = data.encode('ascii')  # data should be bytes
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
    the_page = response.read()


# parse page to get form data
soup = BeautifulSoup(the_page, 'html.parser')
viewstate = soup.select("#__VIEWSTATE")[0]['value']
viewstategen = soup.select("#__VIEWSTATEGENERATOR")[0]['value']
viewValid = soup.select("#__EVENTVALIDATION")[0]['value']

# find value for 3 date choice and update form data
Foreclosure_dates = soup.find_all('ul')
Foreclosure_date = Foreclosure_dates[8].find_all('li')[3].text.strip()
Foreclosure_ch = re.findall(r'[^/]+(?://[^/]*)*', Foreclosure_date)
date = Foreclosure_ch[0]+"%2F"+Foreclosure_ch[1]+"%2F"+Foreclosure_ch[2]
eventag = {"type": 1, "index": 3, "text": "", "value": ""}
eventag['text'] = date
eventag

# formdata with date choice
formData = (
    ('__VIEWSTATE', viewstate),
    ('__VIEWSTATEGENERATOR', viewstategen),
    ('__EVENTTARGET', 'ddlDate'),
    ('__EVENTARGUMENT', eventag),
    ('ToolkitScriptManager1_TSM', viewTSM),
    ('__EVENTVALIDATION', viewValid)
)


# 3rd HTTP request with form data
data = urllib.parse.urlencode(formData)
data = data.encode('ascii')  # data should be bytes
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
    the_page = response.read()

# parse page to get form data
soup = BeautifulSoup(the_page, 'html.parser')
viewstate = soup.select("#__VIEWSTATE")[0]['value']
viewstategen = soup.select("#__VIEWSTATEGENERATOR")[0]['value']
viewValid = soup.select("#__EVENTVALIDATION")[0]['value']

# formdata with go button click
formData = (
    ('__VIEWSTATE', viewstate),
    ('__VIEWSTATEGENERATOR', viewstategen),
    ('btnGo','GO'),
    ('ToolkitScriptManager1_TSM', viewTSM),
    ('__EVENTVALIDATION', viewValid),
    ('ddlDate_ClientState','')
)

# 4th HTTP request with form data
data_fin = urllib.parse.urlencode(formData)
data_fin = data_fin.encode('ascii')  # data should be bytes
req_fin = urllib.request.Request(url, data_fin)
with urllib.request.urlopen(req_fin) as response:
    the_page_fin = response.read()

# parse page to get form data
soup_fin = BeautifulSoup(the_page_fin, 'html.parser')
soup_fin

try:
    fout = open('tmp.htm', 'w')
except:
    print('Could not open output file\n')

fout.writelines(soup.readlines())
fout.close()
