import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# url = "https://www.provigo.ca/food/fruits-vegetables/c/28000?navid=flyout-L2-fruits-vegetables"

# headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}
# response = requests.get(url=url, headers=headers) 

# soup = BeautifulSoup(response.content, 'html.parser')

# #Put soup into a txt file
# html = soup.prettify()  #bs is your BeautifulSoup object
# with open("out.txt","w") as out:
#     for i in range(0, len(html)):
#         try:
#             out.write(html[i])
#         except Exception:
#             1+1

# target_div = soup.find_all("div", class_ ='css-2imjyh')

# # Extract the text content from the div
# if target_div:
#     price_text = target_div.get_text(strip=True)
#     print("Extracted Price:", price_text)
# else:
#     print("Target div not found.")
    




# Set up Chrome WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Load the website
    driver.get('https://www.instacart.ca/store/adonis/storefront')
    time.sleep(3)

    # Click on the element
    driver.find_element(By.CLASS_NAME, 'e-1dw3ejz').click()
    print("Clicked on Element!")
    time.sleep(5)

    # Update the email and password
    email = driver.find_element(By.CLASS_NAME, 'e-134pq6d')
    passwd = driver.find_element(By.NAME, 'password')
    time.sleep(3)

    email.clear()
    email.send_keys('teamchalkeaters@gmail.com')
    time.sleep(2)

    passwd.clear()
    passwd.send_keys('chalkgdhr4$')
    time.sleep(3)

    driver.find_element(By.CLASS_NAME, 'e-ztomkz').click()
    print("Clicked on Element!")


except Exception as ex:
	print(ex)

# finally:
# 	# Close the browser
# 	driver.quit()


# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Parse the HTML content of the page
    
#     soup = BeautifulSoup(response.content, 'html.parser')
#     print(soup.get_text())
#     # Find the elements containing the information you need
#     product_elements = soup.find_all('div', class_='productCardWrapper')
#     print(product_elements)
#     for product in product_elements:
#         # Extract name, price, and quantity information
#         name = product.find('div', class_='productCardInfo').find('div', class_='title').text.strip()
#         price = product.find('span', class_='price').text.strip()
#         quantity = product.find('div', class_='detailsContainer').find('div', class_='unit').text.strip()

#         # Print or store the information
#         print(f"Name: {name}, Price: {price}, Quantity: {quantity}")

# else:
#     print(f"Failed to retrieve the page. Status code: {response.status_code}")