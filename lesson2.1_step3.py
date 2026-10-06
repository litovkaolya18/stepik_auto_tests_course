import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Считываем x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    # 2. Вводим ответ
    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(y)

    # 3. Отмечаем checkbox
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    # 4. Выбираем radiobutton
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    # 5. Нажимаем Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()