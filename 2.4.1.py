from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

# Функция для расчёта значения
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Явное ожидание, пока цена не станет $100
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # Нажимаем кнопку Book
    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    # Получаем значение x и решаем задачу
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    # Вводим ответ в поле
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    # Нажимаем кнопку Submit
    browser.find_element(By.ID, "solve").click()

    # Пауза, чтобы успеть увидеть результат
    time.sleep(10)

finally:
    browser.quit()