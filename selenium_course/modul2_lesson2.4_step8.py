from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    button1 = browser.find_element_by_id("book").click()
    find_x = browser.find_element_by_id("input_value")
    x = find_x.text
    y = calc(x)
    input_y = browser.find_element_by_id("answer")
    input_y.send_keys(y)
    button2 = browser.find_element_by_id("solve").click()
finally:
    time.sleep(10)
    browser.quit()
'''
Задание: ждем нужный текст на странице
Попробуем теперь написать программу,
которая будет бронировать нам дом для отдыха по строго заданной цене.
Более высокая цена нас не устраивает,
а по более низкой цене объект успеет забронировать кто-то другой.

В этой задаче вам нужно написать программу,
которая будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/explicit_wait2.html
Дождаться, когда цена дома уменьшится до $100(ожидание нужно установить не меньше 12 секунд)
Нажать на кнопку "Book"
Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод text_to_be_present_in_element из библиотеки expected_conditions.

Если все сделано правильно и быстро, то вы увидите окно с числом. Отправьте его в качестве ответа на это задание.
'''
