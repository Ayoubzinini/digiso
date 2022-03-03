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
title=[]
city=[]
detail=[]
study=[]
salary=[]
infos=[]
b = webdriver.Chrome(ChromeDriverManager().install())
b.get('https://www.marocannonces.com/categorie/309/Emploi/Offres-emploi/11.html')
doc=b.page_source
soup=BeautifulSoup(doc,'lxml')

container=soup.find_all("div",{"class":"holder"})
for i in container:
    for j in range(0,len(i)+5,1):
        infos.append(j.text.replace('\n','').strip()) 
    for k in range(0,len(infos)+5,1):
        title.append(infos[k].text.replace('\n','').strip())
        city.append(infos[k+1].text.replace('\n','').strip())
        detail.append(infos[k+2].text.replace('\n','').strip())
        study.append(infos[k+3].text.replace('\n','').strip())
        salary.append(infos[k+4].text.replace('\n','').strip())
        