import time
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver

browser = webdriver.Safari()
baseUrl = "https://www.bikewale.com"
brands = ["tvs", "bajaj", "royalenfield", "yamaha", "honda", "hero", "suzuki", "ktm", "jawa", "harleydavidson", "ducati", "kawasaki", ]
bikeData = []
dataDict = {}

# <----------Create Soup Function---------->
def createSoup(url):
    browser.get(url)
    response = browser.page_source
    soup = BeautifulSoup(response, 'html.parser')
    return soup

# <----------Create Spec Dictionary Function---------->
def saveToDict(dict, key, value):
    dict[key] = value

# <----------Save to CSV Function---------->
def saveToCSV(data):
    df = pd.DataFrame(data, columns=['brand', 'url'])
    df.to_csv('bike-data.csv', index=False)

# <----------GoTo Bikes Function---------->
def getDetails(brands):
    for brand in brands:
        bikeListUrl = baseUrl + "/" + brand + "-bikes"
        soup = createSoup(bikeListUrl)

        li = soup.select("ul > li.o-fzptUA")
        for link in li:
            bike = link.find('a')
            if (bike == None):
                continue
            hrefList = bike.get_attribute_list("href")
            for href1 in hrefList:
                bikeLink = href1
            print(bikeLink)
            bikeData.append([brand, bikeLink])

            ### Into single bike page ###

            singleBikePageURL = baseUrl + bikeLink
            soup = createSoup(singleBikePageURL)


# <----------Master Code---------->
getDetails(brands)
saveToCSV(bikeData)