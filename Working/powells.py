from selenium import webdriver
from bs4 import BeautifulSoup
import re

url = 'https://www.powells.co.uk/pembrokeshire-cottages/amroth/pw9015-morgans-retreat'


def get_data(url):
    driver = webdriver.Chrome()
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    return soup

def parse(soup):

    #Extract Data
    cost = soup.find('span', {'class': 'tocc__title--h1 tocc__c--darkgrey'})
    cost_find = cost.findAll('span')




    #Convert to string and seperate
    #Cost Convert
    cost_convered = []
    for x in cost_find:
        cost_convered.append(str(x))
    price_full = cost_convered[0]
    price1 = price_full.replace('<span data-tabsapibooking-enquiry="pricing.total.totalprice">', '')
    price2 = price1.replace('</span>', '')





    print(price2)


soup = get_data(url)
parse(soup)