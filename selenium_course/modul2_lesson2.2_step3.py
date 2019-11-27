import math
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    link = 'http://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)
    #находим оба элемента для суммирования
    x_element = browser.find_element_by_id("num1")
    x_value = x_element.text
    y_element = browser.find_element_by_id("num2")
    y_value = y_element.text
    z = int(x_value) + int(y_value)
    #дальше надо найти нужную сроку в списке
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text('%s' % z)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
'''
Задание: работа с выпадающим списком
Для этой задачи мы придумали еще один вариант капчи для роботов.
Придется немного переобучить нашего робота, чтобы он справился с новым заданием.

Напишите код, который реализует следующий сценарий:

Открыть страницу http://suninjuly.github.io/selects1.html
Посчитать сумму заданных чисел
Выбрать в выпадающем списке значение равное расчитанной сумме
Нажать кнопку "Submit"
Если все сделано правильно и достаточно быстро
(в этой задаче тоже есть ограничение по времени), вы увидите окно с числом.
Отправьте полученное число в качестве ответа для этого задания.

 

Когда ваш код заработает, попробуйте запустить его на странице http://suninjuly.github.io/selects2.html. Ваш код и для нее тоже ﻿должен пройти успешно.
'''
