from os import listdir
from pandas import read_excel, DataFrame, concat
files = listdir('/home/az/Downloads/Scrapper/to_merge/')
df = DataFrame([], columns=["Nom","Adresses","Phones","CP"])
final_name=''
for i in files:
    d=read_excel('/home/az/Downloads/Scrapper/to_merge/'+i)
    try:
        del d['Unnamed: 0']
    except:
        a=2
        del a
    df=concat([df, d], ignore_index = True, axis = 0)
    final_name=final_name+i[0:-5]+'-'
#final_name[0:-1]
df.to_excel('merged'+'.xlsx')