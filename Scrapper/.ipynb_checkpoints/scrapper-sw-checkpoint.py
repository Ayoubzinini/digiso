from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
from pandas import DataFrame
import numpy as np
import string
from random import choice
npns=[]
types_contact=[]
adresses=[]
phones=[]
cp=[]
city=[]
iters=[int(j) for j in range(1,101,1)]
for i in iters:
    b = webdriver.Chrome(ChromeDriverManager().install())
    b.get('https://www.local.ch/fr/q?city=Berne&ext=1&filter%5Bentry_type%5D=private&page='+str(i)+'&rid=Lcc8')
    doc=b.page_source
    soup=BeautifulSoup(doc,'lxml')
    npn=soup.find_all("h2",{"class":"lui-margin-vertical-zero card-info-title"})
    #adresse=soup.find_all("div",{"class":"card-info-address"})
    phone=soup.find_all("span",{"class":"action-button-refuse-advertising"})
    iiters=range(len(npn))
    for k in iiters:
        npns.append(npn[k].text)
        adresses.append(adresse[k].text)
        phones.append(phone[k].text)