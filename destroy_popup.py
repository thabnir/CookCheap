import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
    
def destroy_popup(url):
    
    # https://www.instacart.ca/store/adonis/storefront
    
    # Set up Chrome WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()


    try:
        # Load the website
        driver.get(url)
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

destroy_popup('https://www.instacart.ca/store/adonis/storefront')