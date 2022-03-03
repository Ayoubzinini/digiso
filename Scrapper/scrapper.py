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
from pandas import read_excel
npns=[]
types_contact=[]
adresses=[]
phones=[]
cp=[]
city=[]
b = webdriver.Chrome(ChromeDriverManager().install())
for i in communes:
    i=i.replace('-','+')
    sec=b.get('https://annuaire.118712.fr/?s='+i)
    lt=[5,6,7,8,9,10]
    time.sleep(choice(lt))
    try:
        b.find_element_by_id('didomi-notice-agree-button').click()
    except NoSuchElementException:
        a=2
    e=b.find_element_by_tag_name('body')
    h=[0]
    while True:
        e.send_keys(Keys.PAGE_DOWN)
        st=[0.25,0.27,0.3,0.32,0.34,0.35]
        time.sleep(choice(st))
        nh=b.execute_script('return document.body.scrollHeight;')
        if h.count(max(h))>100:
            break
        else:
            h.append(b.execute_script('return document.body.scrollHeight;'))
            continue
    doc=b.page_source
    soup=BeautifulSoup(doc,'lxml')
    npn=soup.find_all("h2",{"class":"titre"})
    type_contact=soup.find_all("span",{"class":"propart_text"})
    #adresse=soup.find_all("span",{"class":"streetAddress"})
    adresse=soup.find_all("div",{"class":"address"})
    phone=soup.find_all("span",{"itemprop":"telephone"})
    for i in range(len(npn)):
        npns.append(npn[i].text.strip())
        types_contact.append(type_contact[i].text.strip())
        adresses.append(adresse[i].text.strip())
        phones.append(phone[i].text.strip().replace(' ', ''))
    try:
        for i in adresses:
            i=i.replace('\n',' ')
            scp=i.index(',')+2
            ecp=scp+5
            sc=scp+6
            ec=len(i)+1
            cp.append(i[scp:ecp])
            city.append(i[sc:ec])
    except:
        cp.append(np.nan)
        city.append(np.nan)
adrs=[]
for i in adresses:
    adr=''
    for j in i:
        if j=='\n':
            adr=adr+j.replace('\n',' ')
        else:
            adr=adr+j
    adrs.append(adr)
Results=DataFrame([npns,types_contact,adrs,phones]).T
Results.columns=["Nom et Prénom","Type","Adresses","Phones"]
Results=Results[Results.Type=='Particulier']
Results.to_excel("/home/az/Downloads/Scrapper/scrapped.xlsx")
df=read_excel("/home/az/Downloads/Scrapper/scrapped.xlsx")
del df['Unnamed: 0']
cp=[]
city=[]
for i in df.Adresses:
    if ', ' in i:
        scp=i.index(',')+2
        ecp=scp+5
        sc=scp+6
        ec=len(i)+1
        cp.append(i[scp:ecp])
        city.append(i[sc:ec])
    else:
        cp.append(i[0:5])
        city.append(i[6:len(i)])
df["Villes"]=city
df["CP"]=cp
df[[str(i).startswith(dep_cible) for i in df.CP]]
df.to_excel("/home/az/Downloads/Scrapper/scrapped.xlsx")