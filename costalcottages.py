from selenium import webdriver
from bs4 import BeautifulSoup
import re

url = 'https://www.coastalcottages.co.uk/cottages/plumstone-view-cottage/?ref=23487'


def get_data(url):
    driver = webdriver.Chrome()
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    return soup

def parse(soup):

    #Extract Data
    cost_full = soup.find('div', {'class': 'available-weeks'})
    print(cost_full)
    cost = cost_full.findAll('strong')
    print(cost)
    






    #Convert to string and seperate
    #Cost Convert
    
    for x in cost:
        new_cost = str(x)
        filtered_text = new_cost.replace('strong', '')
        print(filtered_text)
        











soup = get_data(url)
parse(soup)