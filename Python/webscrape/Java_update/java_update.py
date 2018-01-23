from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import re

Ver = "https://java.com/en/download/"


verClient =  uReq(Ver)
ver_html = verClient.read()
verClient.close()
ver_soup = soup(ver_html, "html.parser")
ver_txt = ver_soup.h4.text.strip()
ver_number = re.findall(r'\d{3}',ver_txt)

DL = "https://filestore.techygeekshome.info/download/java-8-update-%s-offline-msi-installer-all-in-one-package/" % ver_number[0]
dl_client = uReq(DL)
dl_html = dl_client.read()
dl_client.close()
dl_soup = soup(dl_html, "html.parser")
link = dl_soup.findAll("a",{"class":"wpdm-download-link"})[0].get('onclick')
link = re.findall(r"'.*?'", link)
link = link[0].strip("'")

for link in soup.find_all('a'):
    print(link.get('href'))
