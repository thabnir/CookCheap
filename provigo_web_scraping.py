import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# url = "https://www.provigo.ca/concombres-anglais/p/20070132001_EA"
url = "https://www.provigo.ca/carottes-sac-de-3-lb/p/20600927001_EA"

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
        name_text = "-1"
        print("Name not found.")

    if price:
        price_text = price.get_text(strip=True)
        print("Extracted Price:", price_text)
    else:
        price_text = "-1"
        print("Price not found.")

    if quantity:
        quantity_text = quantity.get_text(strip=True)
        print("Extracted Quantity:", quantity_text)
    else:
        quantity_text = "-1"
        print("Quantity not found.")

    print("Url: ", url)

    #{"Cucumber": {"Price": " 1,99", "Quantity": "1", "url": "cucumber.com"}, "Potato":{"Price": 6, "Quantity": "100g", "url": "potato.com"}}
    info = dict(Price = price_text, Quantity = quantity_text, Url = url)
    info = {name_text: info}
    print(info)
    return info

# get_info(url)

#Write function that can search for a certain produce on provigo website
def get_url(name_produce):
    '''(str) --> (str)
    Given the name of a product, output the url of the page containing said product
    '''
    search_url = f"https://www.provigo.ca/search?search-bar={name_produce}"
    driver = webdriver.Chrome()

    try:
        driver.get(search_url)

        # Wait for the page to load (adjust the wait time as needed)
        driver.implicitly_wait(20)

        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')

        # #Put soup into a txt file, good for debugging hehe
        html = soup.prettify()  #soup is your BeautifulSoup object
        with open("out.txt","w") as out:
            for i in range(0, len(html)):
                try:
                    out.write(html[i])
                except Exception:
                    1+1

        #Triage by cheapest to most expensive and then grab cheapest item
        # dropdown = driver.find_element(By.CLASS_NAME, "MuiSvgIcon-root styled-dropdown__selected-item__icon")
        # dropdown.click
        # button = driver.find_element(By.CSS_SELECTOR, "button[data-option-value='price-asc']")
        # button.click
        # print("WOOT")
        # link = soup.find('a', class_ ="product-tile__details__info__name__link")['href']
        # print(link)
        # link_element = soup.find('a', class_='product-tile__details__info__name__link')

        # # Extract the href attribute
        # if link_element:
        #     href_link = link_element.get('href')
        #     print("Href link:", href_link)
        # else:
        #     print("No matching element found.")

        # return link

    finally:
        driver.quit()

get_url("patate")

# #Put soup into a txt file, good for debugging hehe
# html = soup.prettify()  #soup is your BeautifulSoup object
# with open("out.txt","w") as out:
#     for i in range(0, len(html)):
#         try:
#             out.write(html[i])
#         except Exception:
#             1+1
