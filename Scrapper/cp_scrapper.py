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
Nom=[]
Code_postal=[]
Endroint=[]
b = webdriver.Chrome(ChromeDriverManager().install())
time.sleep(0.5)
ville=input('Ville : ')
b.get('https://codes-postaux.cybo.com/search/?q='+ville+'&pl=&i=&t=')
doc=b.page_source
soup=BeautifulSoup(doc,'lxml')
table=soup.find_all("div",{"class":"l sitem"})
l=list(set([i.text[0:3] for i in table]))
