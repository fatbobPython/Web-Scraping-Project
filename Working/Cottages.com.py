
from selenium import webdriver
from bs4 import BeautifulSoup
import re

url = 'https://www.cottages.com/cottages/sealock-cottage-uk35048?nights=7&range=3&adult=2&infant=0'


def get_data(url):
    driver = webdriver.Chrome()
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    return soup

def parse(soup):

    #Extract Data
    cost = soup.find(id = 'nowprice')
    title = soup.find('h2', {'class': 'c-dark-grey seo-property-name'})


    #Convert to string and seperate
    #Cost Convert
    cost_convered = []
    for x in cost:
        cost_convered.append(str(x))
    price = cost_convered[1]
    int_price = int(price)

    #Name Convert
    name_convert = []
    for x in title:
        name_convert.append(str(x))
    name = name_convert
    print(name, ':', int_price)




soup = get_data(url)
parse(soup)
