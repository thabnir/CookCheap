import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

# url = "https://www.provigo.ca/concombres-anglais/p/20070132001_EA"
# url = "https://www.provigo.ca/carottes-sac-de-3-lb/p/20600927001_EA"



def get_info(url, driver):
    # driver = webdriver.Chrome()
    driver.get(url)

    time.sleep(5)
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')

    name = soup.find("h1", class_='product-name__item product-name__item--name')
    price = soup.find("span", class_ ='price__value selling-price-list__item__price selling-price-list__item__price--now-price__value')
    quantity = soup.find("span", class_ = 'price__unit comparison-price-list__item__price__unit')

    # Extract the text content
    if name:
        name_text = name.get_text(strip=True)
        # print("Extracted Name:", name_text)
    else:
        name_text = "-1"
        print("Name not found.")

    if price:
        price_text = price.get_text(strip=True)
        #print("Extracted Price:", price_text)
    else:
        price_text = "-1"
        print("Price not found.")

    if quantity:
        quantity_text = quantity.get_text(strip=True)
        #print("Extracted Quantity:", quantity_text)
    else:
        quantity_text = "-1"
        #print("Quantity not found.")

    #print("Url: ", url)

    #{"Cucumber": {"Price": " 1,99", "Quantity": "1", "url": "cucumber.com"}, "Potato":{"Price": 6, "Quantity": "100g", "url": "potato.com"}}
    info = dict(Price = price_text, Quantity = quantity_text, Url = url)
    print(info)
    return name_text, info

#Write function that can search for a certain produce on provigo website
def get_url(name_produce, driver):
    '''(str) --> (str)
    Given the name of a product, output the url of the page containing said product
    '''
    search_url = f"https://www.provigo.ca/search?search-bar={name_produce}"
    # driver = webdriver.Chrome()
    driver.get(search_url)

    # Wait for the page to load (adjust the wait time as needed)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "product-tile__details__info__name__link"))
    )
    revealed = driver.find_element(By.CLASS_NAME, 'product-tile__details__info__name__link')

    wait = WebDriverWait(driver, timeout=2)
    wait.until(lambda d : revealed.is_displayed())

    html = driver.page_source
    # time.sleep(30) #Keeps browser open, debugging purposes
    driver.quit()

    soup = BeautifulSoup(html, 'html.parser')

    link = soup.find("a", class_="product-tile__details__info__name__link")['href']
    link = "https://www.provigo.ca"+link
    print(link)
    return link


###Use case: Get info for "saumon"
# url = get_url("patate")
# get_info(url)

#Given a list of ingredients needed, output a dictionary with all of their info
def provigo_info(ingredients):
    '''(list of strings) --> dict
    '''
    provigo = {}
    for ingredient in ingredients:
        url = get_url(ingredient)
        name, info = get_info(url)
        #If we cannot find a produce, don't include in the dictionary
        if name == -1:
            continue
        provigo.update({name: info})
    
    return provigo

a = provigo_info(['egg', 'non-fat yogurt', 'baking soda', 'cinnamon', 'raisins', 'banana', 'carrots'])
print(a)


driver.quit()
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

# #Put soup into a txt file, good for debugging hehe
# html = soup.prettify()  #soup is your BeautifulSoup object
# with open("out.txt","w") as out:
#     for i in range(0, len(html)):
#         try:
#             out.write(html[i])
#         except Exception:
#             1+1
