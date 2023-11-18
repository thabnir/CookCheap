import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://www.provigo.ca/concombres-anglais/p/20070132001_EA"

def get_info(url):
    driver = webdriver.Chrome()
    driver.get(url)

    time.sleep(5)
    html = driver.page_source
    driver.quit()

    soup = BeautifulSoup(html, 'html.parser')

    name = soup.find("h1", class_='product-name__item product-name__item--name')
    price = soup.find("span", class_ ='price__value selling-price-list__item__price selling-price-list__item__price--now-price__value')
    quantity = soup.find("span", class_ = 'price__unit comparison-price-list__item__price__unit')

    # Extract the text content
    if name:
        name_text = name.get_text(strip=True)
        print("Extracted Name:", name_text)
    else:
        print("Name not found.")

    if price:
        price_text = price.get_text(strip=True)
        print("Extracted Price:", price_text)
    else:
        print("Price not found.")

    if quantity:
        quantity_text = quantity.get_text(strip=True)
        print("Extracted Quantity:", quantity_text)
    else:
        print("Quantity not found.")

    print("Url: ", url)

get_info(url)
# #Put soup into a txt file, good for debugging hehe
# html = soup.prettify()  #soup is your BeautifulSoup object
# with open("out.txt","w") as out:
#     for i in range(0, len(html)):
#         try:
#             out.write(html[i])
#         except Exception:
#             1+1
