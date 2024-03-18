import time
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver

browser = webdriver.ChromiumEdge()

baseUrl = "https://www.bikedekho.com"
brands = ["tvs", "bajaj", "royal-enfield", "yamaha", "honda", "hero", "suzuki", "ktm", "jawa", "harley-davidson", "ducati", "kawasaki", ]
bikeUrls = []
for brand in brands:
    url = baseUrl + "/" + brand + "-bikes"
    print(url)
    browser.get(url)
    # time.sleep(10)
    response = browser.page_source
    # browser.quit()
    soup = BeautifulSoup(response, 'html.parser')
    li = soup.select("ul.bikelist > li")
    for link in li:
        bike = link.find('a')
        print(bike)
        bikeUrls.append([bike])
        # time.sleep(2)
    print("Brand: " + brand + "Done")