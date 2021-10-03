from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import date, timedelta, datetime

url = 'https://www.sykescottages.co.uk/cottage/Scottish-Borders-Gaindykehead/Blackbrae-Cabin-982863.html'


def extract_prices_from_page(year, soup):
    booking_buttons = soup.select('ul.booking-buttons>li>div.inner-button')[1:]
    for btn in booking_buttons:
        date_str = next(iter(btn.select('p.date>span'))).string[:-3]
        dte = datetime.strptime(f'{date_str} {year}', '%a %d %b %Y')

        price = next(iter(btn.select('p.price'))).string
        # this is where we save to database - using a reference to the price
        # monitor config, the current date, and the date and price for the
        # property
        print(f'{dte} {price}')


def first_of_next_month(dte):
    return (dte.replace(day=1) + timedelta(days=32)).replace(day=1)


def configure_driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(url)
    return driver


def click_next_month(driver):
    next_month = driver.find_element_by_css_selector('a.next-month')
    driver.execute_script('arguments[0].scrollIntoView(true)', next_month)
    next_month.click()


def find_prices(url):
    driver = configure_driver()

    dte = date.today()
    while dte < (date.today() + timedelta(weeks=52)):
        soup = BeautifulSoup(driver.page_source, "html.parser")
        extract_prices_from_page(dte.year, soup)
        dte = first_of_next_month(dte)
        click_next_month(driver)


find_prices(url)
