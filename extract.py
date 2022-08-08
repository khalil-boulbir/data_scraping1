from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException  
from bs4 import BeautifulSoup
import requests
import random
import pandas as pd
import time
x=random.randint(1,3)
name=[]
industry=[]
company=[]
meet=[]
areas=[]
country=[]
investsment=[]
portfilio=[]
p_activity=[]
s_activity=[]
avreage=[]
data=open('links.txt','r')
df=data.readlines()

for i in range(1,2):
    webpage = requests.get(df[i])
    soup = BeautifulSoup(webpage.text, "html.parser")
    name.append(soup.find("span", {"class": "nome-texto"}).text.replace("\n","").strip())
    industry.append(soup.find("span", {"class": "cargo"}).text.replace("\n","").strip())
    company.append(soup.find("span", {"class": "empresa"}).text.replace("\n","").strip())
    #areas.append(soup.find("").text)    
    time.sleep(5)
    driver = webdriver.Chrome()
    driver.get("https://www.griclub.org/home?member_login_status=logout&title=Logout+success&msg=Logout+from+GRI+Club+site+successfully%21")
    
    time.sleep(30)
    driver.get(df[i])
    time.sleep(2)
    def check_exists_by_xpath1(xpath):
        try:
            driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True
    if(check_exists_by_xpath1("//div[contains(@class,'infos 0')]")==True):
        meet.append(driver.find_element_by_xpath("//div[contains(@class,'infos 0')]").text[115:].replace("\n"," "))
        print("yes")
    else:
        meet.append("NA")
   
    if(check_exists_by_xpath1("//div[contains(@class,'infos 2')]")==True):
        areas.append(driver.find_element_by_xpath("//div[contains(@class,'infos 2')]").text[41:].replace("\n"," "))
        print("yes")
    else:
        print("no")
        areas.append("NA")
    if(check_exists_by_xpath1("//div[contains(@class,'infos 4')]")==True):
        country.append(driver.find_element_by_xpath("//div[contains(@class,'infos 4')]").text[69:].replace("\n"," "))
    else:
        country.append("NA")
    if(check_exists_by_xpath1("//div[contains(@class,'infos 6')]")==True):
        investsment.append(driver.find_element_by_xpath("//div[contains(@class,'infos 6')]").text[44:].replace("\n","  "))
    else:
        investsment.append("NA")
    if(check_exists_by_xpath1("//div[contains(@class,'infos 7')]")==True):
        portfilio.append(driver.find_element_by_xpath("//div[contains(@class,'infos 7')]").tex[47:]t.replace("\n",""))
    else:
        portfilio.append("NA")
    if(check_exists_by_xpath1("//div[contains(@class,'infos 8')]")==True):
        p_activity.append(driver.find_element_by_xpath("//div[contains(@class,'infos 8')]").text[30:].replace("\n"," "))
    else:
        p_activity.append("NA")
    if(check_exists_by_xpath1("//div[contains(@class,'infos 9')]")==True):
        s_activity.append(driver.find_element_by_xpath("//div[contains(@class,'infos 9')]").text[60:].replace("\n"," "))
    else:
        s_activity.append("NA")
    if(check_exists_by_xpath1("//div[contains(@class,'infos 10')]")==True):
        avreage.append(driver.find_element_by_xpath("//div[contains(@class,'infos 10')]").text[39:].replace("\n",""))
    else:
        avreage.append("NA")
    time.sleep(1)
    driver.close()
data={"senior decision-makers":meet,"areas interested":areas
," countries or cities interested":country
," investment strategies":investsment
,"trategy regarding portfolio":portfilio
,"primary activity":p_activity
," secondary activity":s_activity," current average ":avreage)

df=pd.DataFrame(data)
df.to_csv("meet.csv")

