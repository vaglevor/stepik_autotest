from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    value = browser.find_element(By.TAG_NAME, "img")
    value1 = value.get_attribute('valuex')
    x_element = value1
    x = x_element
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, "[type='text']")
    input1.send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    option2.click()
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

