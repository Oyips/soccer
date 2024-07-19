#Home and away

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import os

print("hello")
url="https://www.soccerstats.com/homeaway.asp?league=brazil"

page=requests.get(url)

soup=BeautifulSoup(page.text,"html.parser")



a=[]
c=[]


for g in range(2):
    table=soup.find_all("table",id="btable")[g]
    row=table.find_all("tr")
    for i in row:
        b=[]
        for j in i.find_all(["td","th"]):
            b.append(j.get_text(separator="|",strip=True))
        if g==0:
            a.append(b)
        else:
            c.append(b)
    
    



header=a[0]
data=a[1:]
df=pd.DataFrame(columns=header,data=data)

header=c[0]
data=c[1:]
df1=pd.DataFrame(columns=header,data=data)
df.to_csv("home_brazil.csv",index=False)
df1.to_csv("away_brazil.csv",index=False)
print(df)
print("")
print(df1)



