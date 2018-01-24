from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import re
import itertools
import string

#file process

url = 'https://weedmaps.com/doctors/doctor-bonanno-2'

#Load/GET the java home webpage to get current version #
verClient =  uReq(url)

#read the java home webpage into a variable
ver_html = verClient.read()

#close the connection
verClient.close()

#parse the java home webpage with beautiful soup
ver_soup = soup(ver_html, "html.parser")