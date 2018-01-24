from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import re
import itertools
import string


#using the builtin iterate function to creat a list of word permutation using the string.ascii_letters
#for possible values of a work of length size.
#keywords = [''.join(i) for i in itertools.product(string.ascii_lowercase, repeat=2)]

#for key in keywords:

#file process
filename = "MLS-NJ.csv"
f = open(filename,"w")
headers = "Realtor Name, Realtor_agency, Realtor_title, Realtor_office_phone, Realtor_contact_phone, Realtor_email\n"

f.write(headers)

url = 'http://www.njmls.com/members/index.cfm?action=dsp.results&city=&county=&nametype=lastname&name=%s&x=0&y=0' % 'ba'

#Load/GET the java home webpage to get current version #
verClient =  uReq(url)

#read the java home webpage into a variable
ver_html = verClient.read()

#close the connection
verClient.close()

#parse the java home webpage with beautiful soup
ver_soup = soup(ver_html, "html.parser")

#use beautiful soup to find the heading needed and remove non text chars
listings = ver_soup.findAll("div",{"class":"realtor-info"})

#listing = listings[0]

for listing in listings:
    try:
        Realtor_name = re.findall(r'<strong>(.*?)</strong>',str(listing))[0]
    except:
        Realtor_name = ""
    try:
        Realtor_agency = re.findall(r'<strong>(.*?)</strong>',str(listing))[1]
    except:
        Realtor_agency = ""
    try:
        Realtor_title = re.findall(r'left;\">\n(.*?)<br',str(listing))[0].strip()
    except:
        Realtor_title = ""
    try:
        Realtor_office_phone = re.findall(r'Office Phone:\s(.*?)<br',str(listing))[0]
    except:
        Realtor_office_phone = ""
    try:
        Realtor_contact_phone = re.findall(r'Contact Phone:\s(.*?)<br',str(listing))[0]
    except:
        Realtor_contact_phone = ""
    try:
        mail = listing.a["href"]
        Realtor_email = re.findall(r'mailto:(.*?)\?',str(mail))[0]
    except:
        Realtor_email = ""


    f.write(Realtor_name + "," + Realtor_agency.replace(",", "-") + "," + Realtor_title + "," + Realtor_office_phone + "," + Realtor_contact_phone + "," + Realtor_email + "\n")


f.close()