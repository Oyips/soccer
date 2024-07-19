
import requests
from bs4 import BeautifulSoup
import os
import pandas as pd
import numpy


print("hello")
url="https://www.soccerstats.com/table.asp?league=usa&tid=rp"

site=requests.get(url)

soup=BeautifulSoup(site.text,"html.parser")

Table=soup.find("table",id="btable")

Row=Table.find_all("tr")
a=[]
for i in Row:
    b=[]
    for k in i.find_all(["th","td"]):
        b.append(k.get_text(separator=" | ",strip=True))
    a.append(b)
header=a[0]
data=a[1:]
df=pd.DataFrame(data=data)

df.columns=df.loc[0,:]
df=df.drop([0])

#df=df.drop(["Stats"],axis=1)
print(df)
df.to_csv("usa_rp.csv",index=True)

