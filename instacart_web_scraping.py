import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# from destroy_popup import destroy_popup
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from csv import writer
import os


def get_info_instacart(url):
    driver = webdriver.Chrome()
    driver.get(url)

    time.sleep(5)
    html = driver.page_source
    driver.quit()

    soup = BeautifulSoup(html, "html.parser")

    name = soup.find("span", class_="e-17kpahp")

    price = soup.find("span", class_="e-1ls9hv7")
    if not price:
        price = soup.find("span", class_="e-0")

    if price:
        quantity = price.get_text(strip=True)
        try:
            quantity = quantity.split("/")[1]
        except IndexError:
            quantity = "per pack"
    else:
        quantity = 0

    unitprice = soup.find("div", class_="e-1og1nqr")
    if unitprice:
        unit = unitprice.get_text(strip=True)
        try:
            unit = unit.split("/")[1]
        except IndexError:
            unit = "per unit"
    else:
        unit = 0

    # Extract the text content
    if name:
        name_text = name.get_text(strip=True)
        print("Extracted Name:", name_text)
    else:
        name_text = "-1"
        print("Name not found.")

    if price:
        price_text = price.get_text(strip=True)
        try:
            price_text = float(price_text.split("/")[0][1:])
        except ValueError:
            price_text = float(price_text.split()[0][1:])
        print("Extracted Price:", price_text)
    else:
        price_text = "-1"
        print("Price not found.")

    if quantity:
        quantity_text = quantity
        print("Extracted Quantity:", quantity_text)
    else:
        quantity_text = "-1"
        print("Quantity not found.")

    if unitprice:
        unit_price = unitprice.get_text(strip=True)
        try:
            unit_price = float(unit_price.split("/")[0][1:])
        except ValueError:
            unit_price = float(unit_price.split()[0][1:])
        print("Extracted Unit Price:", unit_price)
    else:
        unit_price = "null"
        print("Unit price not found.")

    if unit:
        print("Extracted Unit:", unit)
    else:
        unit = "null"
        print("Unit not found.")

    print("Url: ", url)

    info = dict(
        Price=price_text,
        Quantity=quantity_text,
        UnitPrice=unit_price,
        Unit=unit,
        Url=url,
    )
    print(info)
    return name_text, info


def get_url_instacart(name_produce, store):
    """(str, str) --> (str)
    name_produce: name of food to search
    store: metro, adonis, costco-canada, super-c, walmart-canada
    Given the name of a product, output the url of the page containing said product
    """
    search_url = f"https://www.instacart.ca/store/{store}/s?k={name_produce}"
    driver = webdriver.Chrome()
    driver.get(search_url)

    # Wait for the page to load (adjust the wait time as needed)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "e-1dlf43s"))
    )
    revealed = driver.find_element(By.CLASS_NAME, "e-1dlf43s")

    wait = WebDriverWait(driver, timeout=2)
    wait.until(lambda d: revealed.is_displayed())

    html = driver.page_source
    # time.sleep(30) #Keeps browser open, debugging purposes
    driver.quit()

    soup = BeautifulSoup(html, "html.parser")

    link = soup.find("a", class_="e-1dlf43s")["href"]
    link = "https://www.instacart.ca" + link
    print(link)
    return link


def instacart_info(ingredients, store):
    """(list of strings) --> dict"""
    instacart = {}
    for ingredient in ingredients:
        url = get_url_instacart(ingredient, store)
        name, info = get_info_instacart(url)
        # If we cannot find a produce, don't include in the dictionary
        if name == -1:
            continue
        instacart.update({name: info})

    return instacart


# instacart_info(['mango', 'pineapple', 'kiwi', 'pesto sauce'], 'provigo')
