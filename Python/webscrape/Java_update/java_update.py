from bs4 import BeautifulSoup as soup
from urllib.request import urlretrieve as uRet
from urllib.request import urlopen as uReq
import re
import zipfile
from os.path import exists
import os.path


Ver = "https://java.com/en/download/"
dir = "Z:\Installers"

#Load/GET the java home webpage to get current version #
verClient =  uReq(Ver)

#read the java home webpage into a variable
ver_html = verClient.read()

#close the connection
verClient.close()

#parse the java home webpage with beautiful soup
ver_soup = soup(ver_html, "html.parser")

#use beautiful soup to find the heading needed and remove non text chars
ver_txt = ver_soup.h4.text.strip()

#use regex to get numbers with 3 digits
ver_number = re.findall(r'\d{3}',ver_txt)

#files to replace or check for
java_files = ["jre1.8.0_%s.msi" % ver_number[0], "jre-8u%s-windows-i586.exe" % ver_number[0]]

#check if java files are current
if exists(dir+java_files[1]) and exists(dir+java_files[0]) == True:
    exit

else:
    #delete old java files
    
    files = os.listdir(dir)
    for file in files:
        if file.startswith("jre"):
            os.remove(os.path.join(dir,file))

    DL = "https://filestore.techygeekshome.info/download/java-8-update-%s-offline-msi-installer-all-in-one-package/" % ver_number[0]
    dl_client = uReq(DL)
    dl_html = dl_client.read()
    dl_client.close()
    dl_soup = soup(dl_html, "html.parser")

    #uer regex to find a tag and choose list item 0, then pic attribute onclick
    link = dl_soup.findAll("a",{"class":"wpdm-download-link"})[0].get('onclick')

    #use regex to find all chars between single quotes
    link = re.findall(r"'.*?'", link)

    #strip excess quotation marks
    link = link[0].strip("'")


    #use urlib to retrive zipfile
    uRet (link, "Z:\Installers\java%s.zip" % ver_number[0])


    #add zip file to variable
    zip = zipfile.ZipFile('java%s.zip' % ver_number[0])

    #extract specified files
    for j in java_files:
        zip.extract(j)
    
    zip.close()

    #remove zip file
    files = os.listdir(dir)
    file = 'java%s.zip' % ver_number[0]
    os.remove(os.path.join(dir,file))