###A Simple web scrapper which print latest news from web

##Do not use for making too many request. Use for learning purpose 

#To get connect and get data from web
import requests

#To parse and use relevant  data 
from bs4 import BeautifulSoup

#to display data beautifully and make them easy to understand
import pandas as pd

#connecting and getting the HTML page data
page=requests.get("http://indianexpress.com/")

#parsing the page
soup=BeautifulSoup(page.content,'html.parser')

#accessing the relevant data using class TAG
right_part=soup.find(class_="right-part bg")

#accessing the relevant data using li TAG
data=right_part.find_all('li')

#Making a list of relevant data
latest_news=[l_news.get_text() for l_news in data]

#Using pandas to display data in table format
Top_latest_feed=pd.DataFrame({"Latest news":latest_news})

print(Top_latest_feed)
