from selenium import webdriver
from selenium.webdriver.chrome.service import Service


#define the website
website = "https://medium.com/tag/technology" 

#define the path where download chromedrive.exe
path = (r"\Users\Narsil\Downloads\chromedriver.exe") #put r before your normal string it converts normal string to raw string

service = Service(executable_path=path)

#create a driver 
driver = webdriver.Chrome(service=service) 

#open driver 

driver.get(website)

