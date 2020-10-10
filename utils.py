"""
Author      : Shrikant pathak
Created At  : 09 July 2019
Description : Common function which is used in the program
"""
from bs4 import BeautifulSoup
from selenium import webdriver
import re

# regex for number and char only
CHECK_RE = re.compile('[a-zA-Z0-9_-]+$')

# function to check  the driver info
def getDriverInfo(path):
   return webdriver.Chrome(path)

# function to check  html source
def getHtmlSource(url,browser):
    browser.get(url)
    html_source = browser.page_source
    return BeautifulSoup(html_source,"html.parser")

# function to check json from html
def getJsonFromHtml(div):
    productList = []
    for x in div :
        if x.find('span',{'class' : 'a-price-whole'}) and  x.find('span',{'class' : 'a-size-medium'}) and len(x.contents)==3 :
            price= "find the price"
            name=x.find('span',{'class' : 'a-size-medium'}).get_text()
            productList.append({"name":name,"price":price})
    return productList

# function to check for special characte in string
def specialCharCheck(data):
    match=CHECK_RE.match(data)
    if match == None :
        return True
    else :
        return False
