from selenium import webdriver
from bs4 import BeautifulSoup
import re

url = 'https://www.sykescottages.co.uk/cottage/Scottish-Borders-Gaindykehead/Blackbrae-Cabin-982863.html?_hsearch=2109156142460f7f6df&_price=247&_display=1#duration=3&start=2021-10-03&changeover=0'


def get_data(url):
    driver = webdriver.Chrome()
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    return soup

def parse(soup):

    #Extract Data
    cost = soup.find('p', {'class': 'price ng-binding'})
    title = soup.find('h1')



    #Convert to string and seperate
    #Cost Convert
    cost_convered = []
    for x in cost:
        cost_convered.append(str(x))
    price = cost_convered[0]
    price.replace('[', '')
    price.replace(']', '')


    #Name Convert
    name_convert = []
    for x in title:
        name_convert.append(str(x))
    name = name_convert[0]
    name.replace('[', '')
    name.replace(']', '')

    print(name, ':', price)


soup = get_data(url)
parse(soup)