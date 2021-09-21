from selenium import webdriver
from bs4 import BeautifulSoup
import re

url = 'https://www.qualitycottages.co.uk/wales/west-wales/cardiganshire/cardigan-bay/tresaith/nyth-bran'


def get_data(url):
    driver = webdriver.Chrome()
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    return soup

def parse(soup):

    #Extract Data
    cost = soup.find(id = 'property__prices')
    cost_find = cost.findAll('strong')




    #Convert to string and seperate
    #Cost Convert
    cost_convered = []
    for x in cost_find:
        cost_convered.append(str(x))
    price_full = cost_convered[0]
    price1 = price_full.replace('<strong>', '')
    price2 = price1.replace('</strong>', '')
    final_price = price2.replace('£', '')




    print(final_price)


soup = get_data(url)
parse(soup)