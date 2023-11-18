import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# url = "https://www.instacart.ca/store/adonis/products/16614423"
#url = "https://www.instacart.ca/store/adonis/products/2594323"
url = "https://www.instacart.ca/store/adonis/products/16614400"

def get_info(url):
    driver = webdriver.Chrome()
    driver.get(url)

    time.sleep(5)
    html = driver.page_source
    driver.quit()

    soup = BeautifulSoup(html, 'html.parser')

    name = soup.find("span", class_='e-17kpahp') 
    price = soup.find("span", class_ ='e-1ls9hv7')
    # quantity = soup.find("span", class_ = 'price__unit comparison-price-list__item__price__unit')

    # Extract the text content
    if name:
        name_text = name.get_text(strip=True)
        print("Extracted Name:", name_text)
    else:
        name_text = "-1"
        print("Name not found.")

    if price:
        price_text = price.get_text(strip=True)
        print("Extracted Price:", price_text)
    else:
        price_text = "-1"
        print("Price not found.")

    # if quantity:
    #     quantity_text = quantity.get_text(strip=True)
    #     print("Extracted Quantity:", quantity_text)
    # else:
    #     quantity_text = "-1"
    #     print("Quantity not found.")

    print("Url: ", url)

    quantity_text = "hihi"
    #{"Cucumber": {"Price": " 1,99", "Quantity": "1", "url": "cucumber.com"}, "Potato":{"Price": 6, "Quantity": "100g", "url": "potato.com"}}
    info = dict(Price = price_text, Quantity = quantity_text, Url = url)
    info = {name_text: info}
    print(info)
    return info

get_info(url)


# #Put soup into a txt file, good for debugging hehe
# html = soup.prettify()  #soup is your BeautifulSoup object
# with open("out.txt","w") as out:
#     for i in range(0, len(html)):
#         try:
#             out.write(html[i])
#         except Exception:
#             1+1
