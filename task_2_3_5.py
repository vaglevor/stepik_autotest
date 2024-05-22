from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button1 = browser.find_element(By.CSS_SELECTOR, "[class^='trollface']")
    button1.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, "[type='text']")
    input1.send_keys(y)
    button2 = browser.find_element(By.CSS_SELECTOR, "[class^='btn']")
    button2.click()

finally:
    time.sleep(15)
    browser.quit()
    