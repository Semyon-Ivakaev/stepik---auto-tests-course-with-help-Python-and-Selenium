import math
from selenium import webdriver
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/math.html'
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    print(x_element)
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    option = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option.click()
    option1 = browser.find_element_by_css_selector("[for='robotsRule']")
    option1.click()
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
'''
Ваша программа должна выполнить следующие шаги:

Открыть страницу http://suninjuly.github.io/math.html.
Считать значение для переменной x.
Посчитать математическую функцию от x (код для этого приведён ниже).
Ввести ответ в текстовое поле.
Отметить checkbox "I'm the robot".
Выбрать radiobutton "Robots rule!".
Нажать на кнопку Submit.
'''
