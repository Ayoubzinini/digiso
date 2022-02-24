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
adresses=[]
phones=[]
cp=[]
city=[]
target_location=input('Cible : ')
for i in string.ascii_uppercase:
    b = webdriver.Chrome(ChromeDriverManager().install())
    time.sleep(0.25)
    try :
        b.get('https://www.fr.canada411.ca/search/si/1/'+i+'/'+target_location+'+QC/rci-'+target_location)
        doc=b.page_source
        soup=BeautifulSoup(doc,'lxml')
        max_pages=soup.find_all("h1")
        try :
            total =[int(i.text[0:i.text.index(' résultats')].replace(u'\xa0', u'')) for i in max_pages][0]
        except:
            a=2
            del a
        if total%15==0:
            n_pages=total/15
        else:
            n_pages=int(total/15)+1
        for j in range(1,int(n_pages)+1,1):
            time.sleep(0.5)
            b.get('https://www.fr.canada411.ca/search/si/'+str(j)+'/'+i+'/'+target_location+'+QC/rci-'+target_location)
            doc=b.page_source
            soup=BeautifulSoup(doc,'lxml')
            name=soup.find_all("h2",{"class":"c411ListedName"})
            adresse=soup.find_all("span",{"class":"adr"})
            phone=soup.find_all("span",{"class":"c411Phone"})
            for k in range(len(name)):
                npns.append(name[k].text)
                adresses.append(adresse[k].text)
                phones.append(phone[k].text.replace('(','').replace(' ','').replace(')','').replace('-',''))
                cp.append(adresse[k].text[-7:len(adresse[k].text)+1])
    except :
        a=2
        del a
Results=DataFrame([npns,adresses,phones,cp]).T
Results.columns=["Nom","Adresses","Phones","CP"]
Results.to_excel("/home/az/Downloads/Scrapper/to_merge/"+target_location+".xlsx")