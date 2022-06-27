## automation_python_web_scraping
Web automation & Web Scraping:

.- XPath - syntax:

    - Easily key to learn web Scraping with selenium
    - Stands for xml path lenguage
    - Is a query lenguage for selecting nodes from xml document but also in html pages.

    syntax: 
    - //tagName and then write the element name.
      - //tagName[] base on position 
      - //tagName[@attributeName="Value"] specify attributes name like class id 
        - function: 
          - contains() will search for text included inside an element 
            - example: //tagName[contains(@attributeName,"Value")]
              - with logical operators: //tagName[(expression 1) and (expression 2)]
          - stars-with() will search for text at the beginning

.- Testing xpath:
   - https://scrapinghub.github.io/xpath-playground/
     - input: 
       <html>
         <head>
           <title>My page title</title>
         </head>
         <body>
           <h2>Welcome to my <a href="#">page</a></h2>
           <p>This is the first paragraph</p>
           <!-- this is the end -->
         </body>
        </html>
     - xpath: //h2
     - result: <h2>Welcome to my <a href="#">page</a></h2>
     - xpath: //h2/text()
     - result: Welcome to my

.- Special characters:
    - /  select the children from the node set on the left side of this characters.
    - // Specifies that the matching node set should be located at any level within the document
    - //. Specifies the current context should be used (refers to present node)
    - //.. refers to parent node)
    - * a wildcard characters that select all elememts or attributes regardless of names
    - ./* select all the children nodes considering the current context 
    - @ select an attribute
    - () grouping an xpath expression 
    - [n] indicates that a node with index "n" should be selected



# Automate The news: installing Selenium and ChromeDriver

- install ChromeDriver from https://chromedriver.chromium.org/downloads. save the path of the file. will use later.
- pip install selenium
- create a new file news_headlines.py 
- from selenium import webdriver, selenium.webdriver.chrome.service, 
- define the website, define the path where download chromedrive.exe, create a driver, open driver 

