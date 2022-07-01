from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
import os
import sys

app_path = os.path.dirname(sys.executable)

dt = datetime.now()

dt_ = dt.strftime("%m%d%Y") #mmddyy 


#define the website
website = "https://bitcoinmagazine.com/" 

#define the path where download chromedrive.exe
path = (r"\Users\Narsil\Downloads\chromedriver.exe") #put r before your normal string it converts normal string to raw string

#headless-mode 
options = Options()
options.headless = True
service = Service(executable_path=path)

#create a driver 
driver = webdriver.Chrome(service=service, options=options) 

#open driver 

driver.get(website)

#//div[@class="header-module--title--32KBA"]

containers = driver.find_elements(by="xpath", value='//phoenix-ellipsis[@class="m-ellipsis m-card--header"]')  #method: find_element (singular for one element), parameters: by="", value=""
                                                                                                   #to avoid conflict, use simple quotes. 
#//div[@class="inner header-module--wrapper--3HEoJ"]/div/h1

titles = []

links = []

for container in containers:
    title = container.find_element(by="xpath", value='./a/h2').text  #the dot replace the xpath function above and to get only the text, use function .text
    #link = container.find_element(by="xpath", value='./div/ul/li/a').get_attribute("href")
    
    titles.append(title)
    #links.append(link)
    
    
my_dic = {'Title': titles} 


df_headlines = pd.DataFrame(my_dic)

df_headlines.to_csv('headlines1.csv')
df_headlines.to_csv('headlines-headless1.csv') #from headless mode 

 
file_n = f'headlines-{dt_}.csv'

final_path = os.path.join(app_path, file_n)

df_headlines.to_csv(final_path)

driver.quit()