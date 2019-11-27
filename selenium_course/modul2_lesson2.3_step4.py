import math
from selenium import webdriver
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn").click()
    time.sleep(1)
    alert = browser.switch_to.alert
    alert.accept()
    find_x = browser.find_element_by_id("input_value")
    x = find_x.text
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    button2 = browser.find_element_by_css_selector(".btn").click()

finally:
    time.sleep(10)
    browser.quit()
    
'''
Задание: принимаем alert
В этой задаче вам нужно написать программу, которая будет выполнять
следующий сценарий:

Открыть страницу http://suninjuly.github.io/alert_accept.html
Нажать на кнопку
Принять confirm
На новой странице решить капчу для роботов, чтобы получить число с ответом
Если все сделано правильно и достаточно быстро
(в этой задаче тоже есть ограничение по времени), вы увидите окно с числом.
Отправьте полученное число в качестве ответа на это задание.
'''
