from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, "[type='text']")
    input1.send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, "[type='checkbox']")
    option1.click()
    option2 = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(20)
    browser.quit()

