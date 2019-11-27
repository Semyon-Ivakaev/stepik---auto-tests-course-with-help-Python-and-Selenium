from selenium import webdriver
import time
import os

try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Sam")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Gamji")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("blabla@mail.ru")

    element = browser.find_element_by_id("file")#найти кнопку добавления
    current_dir = os.path.abspath(os.path.dirname(__file__))#показываем путь до файла
    file_path = os.path.join(current_dir, 'test.txt')# добавляем к этому пути имя файла 
    element.send_keys(file_path)#добавляем

    button = browser.find_element_by_css_selector("button.btn").click()
    
    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()

'''
В этом задании в форме регистрации требуется загрузить текстовый файл.

Напишите скрипт, который будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/file_input.html
Заполнить текстовые поля: имя, фамилия, email
Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
Нажать кнопку "Submit"
Если все сделано правильно и быстро, вы увидите окно с числом.
Отправьте полученное число в качестве ответа для этого задания.
'''
