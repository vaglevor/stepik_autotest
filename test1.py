import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first_class .first")
    first_name.send_keys("123")
    second_name = browser.find_element(By.XPATH,
                                       '//div[@class="first_block"]//div[@class="form-group second_class"]//input[@class="form-control second"]')
    second_name.send_keys("456")
    email = browser.find_element(By.CSS_SELECTOR, ".form-control.third")
    email.send_keys("777@mail.ru")
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()
    time.sleep(1)
    final_text_element = browser.find_element(By.TAG_NAME, "h1")
    final_text = final_text_element.text
    assert 'Congratulations! You have successfully registered!' == final_text

finally:
    # успеваем скопировать код за 30 секунд
    # time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
