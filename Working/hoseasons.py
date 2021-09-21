from selenium import webdriver
from bs4 import BeautifulSoup
import re

url = 'https://www.hoseasons.co.uk/lodges/canterbury-reach-lodge-retreat-canb?adult=2&nights=7&range=3&start=19-9-2021'


def get_data(url):
    driver = webdriver.Chrome()
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    return soup

def parse(soup):

    #Extract Data
    cost = soup.find('h4', {'class': 'total-price'})


    #Convert to string and seperate
    #Cost Convert
    cost_convered = []
    for x in cost:
        cost_convered.append(str(x))
    price_full = cost_convered[0]
    price = price_full.replace('£', '')





    print(price)


soup = get_data(url)
parse(soup)