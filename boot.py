import pandas as pd 
import numpy as np 
from bs4 import BeautifulSoup
import requests
name_=[]
detail_=[]
adress_=[]
       
for j in range(2):
        
        page =requests.get("https://www.zoopla.co.uk/find-agents/letting-agents/london/?q=London&radius=4&search_source=find-agents/letting-agents&pn="+str(j)).text
        soup = BeautifulSoup (page,"lxml")
        names = soup.findAll('h2', {'class' : 'ui-text-t4'}, limit=None)
        details=soup.findAll('p',attrs={'class' : 'fap-agent-card__profile'}, limit=None)
        adress=soup.findAll("address")
        for  name in names :
                name_.append(name.text.strip())
        for dtail in details:
                detail_.append(dtail.text.strip())
                
        for i in adress:
                adress_.append(i.text.strip())
        print(j)
    
matrix={"name":name_,"profil":detail_,"location":adress_}
data=pd.DataFrame(matrix)
data.to_csv("zabia.xlsx")
print(data)
