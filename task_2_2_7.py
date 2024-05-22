from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "txt1.txt"
    file_path = os.path.join(current_dir, file_name)
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("qwerty")
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
   
finally:
    time.sleep(15)
    browser.quit()

    