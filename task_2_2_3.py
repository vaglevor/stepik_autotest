from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element1 = browser.find_element(By.ID, "num1")
    num1 = x_element1.text
    x_element2 = browser.find_element(By.ID, "num2")
    num2 = x_element2.text
    sum = int(num1)+int(num2)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum))
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

