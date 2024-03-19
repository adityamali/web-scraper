import time
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver

browser = webdriver.ChromiumEdge()
baseUrl = "https://www.bikedekho.com"
brands = ["tvs", "bajaj", "royal-enfield", "yamaha", "honda", "hero", "suzuki", "ktm", "jawa-motorcycles", "harley-davidson", "ducati", "kawasaki", ]
bikeData = []


# <----------Create Soup Function---------->
def createSoup(url):
    browser.get(url)
    response = browser.page_source
    soup = BeautifulSoup(response, 'html.parser')
    return soup


# <----------Save to CSV Function---------->
def saveToCSV(data):
    df = pd.DataFrame(data, columns=['brand', 'url'])
    df.to_csv('bike-data.csv', index=False)



for brand in brands:
    bikeListUrl = baseUrl + "/" + brand + "-bikes"
    soup = createSoup(bikeListUrl)
    li = soup.select("ul.bikelist > li")
    for link in li:
        bike = link.find('a')
        if (bike == None):
            continue
        hrefList = bike.get_attribute_list("href")
        for href1 in hrefList:
            bikeLink = href1
        print(bikeLink)
        # bikeData.append([brand, bikeLink])

        ### Into single bike page ###

        singleBikePageURL = baseUrl + bikeLink
        soup = createSoup(singleBikePageURL)


        # time.sleep(2)
    print("Brand: " + brand + "Done")

saveToCSV(bikeData)