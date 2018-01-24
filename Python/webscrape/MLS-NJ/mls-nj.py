from bs4 import BeautifulSoup as soup
from urllib.request import urlretrieve as uRet
from urllib.request import urlopen as uReq
import re
import zipfile
from os.path import exists
import os.path
import itertools
import string


#using the builtin iterate function to creat a list of word permutation using the string.ascii_letters
#for possible values of a work of length size.
#keywords = [''.join(i) for i in itertools.product(string.ascii_lowercase, repeat=2)]


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

listing = listings[0]

mail = listing.a["href"]

Realtor_name = re.findall(r'<strong>(.*?)</strong>',str(listing))[0]
Realtor_agency = re.findall(r'<strong>(.*?)</strong>',str(listing))[1]
Realtor_title = re.findall(r'(.*?)<br/>',str(listing))[1].strip()
office_phone = re.findall(r'(.*?)<br/>',str(listing))[3].strip()
Realtor_office_phone = re.findall(r':\s(.*)',str(office_phone))[0]
contact_phone = re.findall(r'(.*?)<br/>',str(listing))[4].strip()
Realtor_contact_phone = re.findall(r':\s(.*)',str(contact_phone))[0]
Realtor_email = re.findall(r'mailto:(.*?)\?',str(mail))[0]

print(Realtor_name,'\n',Realtor_agency,'\n',Realtor_title,'\n',Realtor_office_phone,'\n',Realtor_contact_phone,'\n',Realtor_email)



# Ver = "https://java.com/en/download/"
# dir = "Z:\Installers"

# #Load/GET the java home webpage to get current version #
# verClient =  uReq(Ver)

# #read the java home webpage into a variable
# ver_html = verClient.read()

# #close the connection
# verClient.close()

# #parse the java home webpage with beautiful soup
# ver_soup = soup(ver_html, "html.parser")

# #use beautiful soup to find the heading needed and remove non text chars
# ver_txt = ver_soup.h4.text.strip()

# #use regex to get numbers with 3 digits
# ver_number = re.findall(r'\d{3}',ver_txt)

# #files to replace or check for
# java_files = ["jre1.8.0_%s.msi" % ver_number[0], "jre-8u%s-windows-i586.exe" % ver_number[0]]

# #check if java files are current
# if exists(dir+java_files[1]) and exists(dir+java_files[0]) == True:
#     exit

# else:
#     #delete old java files
    
#     files = os.listdir(dir)
#     for file in files:
#         if file.startswith("jre"):
#             os.remove(os.path.join(dir,file))

#     DL = "https://filestore.techygeekshome.info/download/java-8-update-%s-offline-msi-installer-all-in-one-package/" % ver_number[0]
#     dl_client = uReq(DL)
#     dl_html = dl_client.read()
#     dl_client.close()
#     dl_soup = soup(dl_html, "html.parser")

#     #uer regex to find a tag and choose list item 0, then pic attribute onclick
#     link = dl_soup.findAll("a",{"class":"wpdm-download-link"})[0].get('onclick')

#     #use regex to find all chars between single quotes
#     link = re.findall(r"'.*?'", link)

#     #strip excess quotation marks
#     link = link[0].strip("'")


#     #use urlib to retrive zipfile
#     uRet (link, "Z:\Installers\java%s.zip" % ver_number[0])


#     #add zip file to variable
#     zip = zipfile.ZipFile('java%s.zip' % ver_number[0])

#     #extract specified files
#     for j in java_files:
#         zip.extract(j)
    
#     zip.close()

#     #remove zip file
#     files = os.listdir(dir)
#     file = 'java%s.zip' % ver_number[0]
#     os.remove(os.path.join(dir,file))