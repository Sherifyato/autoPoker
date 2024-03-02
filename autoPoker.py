from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:/Users/replace with user name/AppData/Local/Google/Chrome/User Data")

try:
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.facebook.com/pokes")
    pokes = driver.find_elements(By.XPATH, "//span[text()='Poke Back']")
    for i in pokes:
        i.click()
        time.sleep(0.3)

except Exception as e:
    print("Error", e)
finally:
    driver.quit()
