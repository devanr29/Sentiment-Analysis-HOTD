from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# Set path to chromedriver as per your configuration
webdriver_service = Service(r"C:\Users\Lenovo\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")  # Use raw string here

# Choose Chrome Browser
driver = webdriver.Chrome(service=webdriver_service)#, options=chrome_options)

# Open the IMDb reviews page
driver.get('https://www.imdb.com/title/tt11198330/reviews')

#def load_all_reviews():
while True:
    try:
    # Wait for the load more button to be present and clickable
        previous_pagee = load_more_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "ipl-load-more__button"))
        )
        load_more_button.click()
        time.sleep(2)  # Wait for reviews to load
    except Exception as e:
        print("No more load more button or error:", e)
        break
