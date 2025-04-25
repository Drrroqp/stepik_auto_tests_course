from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполнение обязательных полей
    browser.find_element(By.NAME, "firstname").send_keys("Ivan")
    browser.find_element(By.NAME, "lastname").send_keys("Petrov")
    browser.find_element(By.NAME, "email").send_keys("ivan.petrov@example.com")

    # Получаем путь к директории текущего файла и создаем путь к файлу
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "testfile.txt")

    # Создаем пустой текстовый файл, если он ещё не существует
    with open(file_path, "w") as file:
        file.write("")

    # Загрузка файла
    file_input = browser.find_element(By.ID, "file")
    file_input.send_keys(file_path)

    # Клик по кнопке Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # Ждем, чтобы увидеть результат
    time.sleep(5)

finally:
    # Удалим файл после выполнения (по желанию)
    if os.path.exists(file_path):
        os.remove(file_path)

    # Закрытие браузера
    browser.quit()