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
    b.get('https://www.local.ch/fr/q?city=Les+Haudères&ext=1&filter%5Bentry_type%5D=private&page='+str(i)+'&rid=Lcc8')
    doc=b.page_source
    soup=BeautifulSoup(doc,'lxml')
    npn=soup.find_all("h2",{"class":"lui-margin-vertical-zero card-info-title"})
    adresse=soup.find_all("div",{"class":"card-info-address"})
    phone=soup.find_all("a",{"class":"js-gtm-event js-kpi-event action-button text-center hidden-md hidden-lg hidden-print action-button-primary"})
    iiters=range(len(npn))
    for k in iiters:
        npns.append(npn[k].text)
        adresses.append(adresse[k].text)
        try :
            ii=phone[k]['href']
            phones.append(ii[4:len(ii)])
        except :
            phones.append(np.nan)
npns=[str(i).strip() for i in npns]
adresses=[str(i).strip() for i in adresses]
phones=[str(i).strip() for i in phones]
for i in adresses:
    try:
        ib=i.index(', ')+2
        ie=ib+4
        iv=ib+5
        cp.append(i[ib:ie])
        city.append(i[iv:len(i)+1])
    except:
        cp.append(np.nan)
        city.append(np.nan)
df=DataFrame([npns,adresses,phones,cp,city]).T
df.columns=['Nom_Prenom','Adresse','Phone','CP','Ville']
df.to_excel('/home/az/Downloads/Scrapper/scrapped-sw.xlsx')