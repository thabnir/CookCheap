import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from destroy_popup import destroy_popup

# yogurt: works (e-0)
# url = "https://www.instacart.ca/store/adonis/products/17874024"

# ground beef: works (e-0)
# url = "https://www.instacart.ca/store/adonis/products/27953531"

# salmon: works (e-1ls9hv7)
# url = "https://www.instacart.ca/store/adonis/products/27943011"

# strawberries: works (e-0)
# url = "https://www.instacart.ca/store/adonis/products/2656121"

# apples: works (e-0)
# url = "https://www.instacart.ca/store/adonis/products/16614400"

# spaghetti: works (e-1ls9hv7)
# url = "https://www.instacart.ca/store/adonis/products/25578738"

# rice: works (e-0)
# url = "https://www.instacart.ca/store/adonis/products/27343516"

# cheese: works (e-0)
# url = "https://www.instacart.ca/store/adonis/products/27954083"

# butter: works (e-0)
# url = "https://www.instacart.ca/store/adonis/products/27266134"


# two class names that work: e-0 and e-1ls9hv7

def get_info(url):
    driver = webdriver.Chrome()
    driver.get(url)

    time.sleep(5)
    html = driver.page_source
    driver.quit()

    soup = BeautifulSoup(html, 'html.parser')

    name = soup.find("span", class_='e-17kpahp') 

    # price = soup.find("span", class_ ='e-0')
    price = soup.find("span", class_ ='e-1ls9hv7')
    if not price:
        price = soup.find("span", class_ ='e-0')
    
    if price:
        quantity = price.get_text(strip=True)
        try:
            quantity = quantity.split('/')[1]
        except IndexError:
            quantity = "per pack"
    else:
        quantity = 0
        
    unitprice = soup.find("div", class_ ='e-1og1nqr')
    if unitprice:
        unit = unitprice.get_text(strip=True)
        unit = unit.split('/')[1]
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
        # convert from string to float
        # clean
        try:
            price_text = float(price_text.split('/')[0][1:])
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
        unit_price = float(unit_price.split('/')[0][1:])
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

    # quantity_text = "hihi"
    #{"Cucumber": {"Price": " 1,99", "Quantity": "1", "url": "cucumber.com"}, "Potato":{"Price": 6, "Quantity": "100g", "url": "potato.com"}}
    info = dict(Price = price_text, Quantity = quantity_text, UnitPrice = unit_price, Unit = unit, Url = url)
    info = {name_text: info}
    print(info)
    return info

# destroy_popup(url)
get_info(url)


# #Put soup into a txt file, good for debugging hehe
# html = soup.prettify()  #soup is your BeautifulSoup object
# with open("out.txt","w") as out:
#     for i in range(0, len(html)):
#         try:
#             out.write(html[i])
#         except Exception:
#             1+1
