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
names=[]
adresses=[]
m_names=[]
nirpps=[]
geos=[]
phones=[]
c_code=[]
b_days=[]
ages=[]
zodiacs=[]
p_email=[]
users=[]
pwds=[]
sites=[]
pcs=[]
cards=[]
exps=[]
cvvs=[]
companies=[]
posts=[]
tails=[]
weights=[]
blood_fs=[]
t_num=[]
wu_mtcn=[]
mg_mtcn=[]
clrs=[]
cars=[]
b = webdriver.Chrome(ChromeDriverManager().install())
contacts_number=input('Contacts number : ')
for i in range(int(contacts_number)):
    b.get('https://www.fakenamegenerator.com/gen-female-fr-fr.php')
    doc=b.page_source
    soup=BeautifulSoup(doc,'lxml')
    n1=soup.find_all("h3")
    n2=soup.find_all("div",{"class":"adr"})
    n3=soup.find_all("dt")
    n4=soup.find_all("dd")
    names.append([i.text for i in n1][0])
    adresses.append([i.text.strip() for i in n2][0])
    iternals=[i.text.strip() for i in n4][0:-8]
    m_names.append(iternals[0])
    nirpps.append(iternals[1])
    geos.append(iternals[2])
    phones.append(iternals[3])
    c_code.append(iternals[4])
    b_days.append(iternals[5])
    ages.append(iternals[6])
    zodiacs.append(iternals[7])
    p_email.append(iternals[8])
    users.append(iternals[9])
    pwds.append(iternals[10])
    sites.append(iternals[11])
    pcs.append(iternals[12])
    cards.append(iternals[13])
    exps.append(iternals[14])
    cvvs.append(iternals[15])
    companies.append(iternals[16])
    posts.append(iternals[17])
    tails.append(iternals[18])
    weights.append(iternals[19])
    blood_fs.append(iternals[20])
    t_num.append(iternals[21])
    wu_mtcn.append(iternals[22])
    mg_mtcn.append(iternals[23])
    clrs.append(iternals[24])
    cars.append(iternals[25])
cols=[names,adresses,m_names,nirpps,geos,phones,c_code,b_days,ages,zodiacs,p_email,users,pwds,sites,pcs,cards,exps,cvvs,companies,posts,tails,weights,blood_fs,t_num,wu_mtcn,mg_mtcn,clrs,cars]
titles=["Full name","Adress","Mother's maiden name", 'NIRPP', 'Geo coordinates', 'Phone', 'Country code', 'Birthday', 'Age', 'Tropical zodiac', 'Email Address', 'Username', 'Password', 'Website', 'Browser user agent', 'MasterCard', 'Expires', 'CVC2', 'Company', 'Occupation', 'Height', 'Weight', 'Blood type', 'UPS tracking number', 'Western Union MTCN', 'MoneyGram MTCN', 'Favorite color', 'Vehicle']
df=DataFrame(dict(zip(titles,cols)))
df.to_excel('/home/az/Downloads/Scrapper/scrapped_fake_identities.xlsx')