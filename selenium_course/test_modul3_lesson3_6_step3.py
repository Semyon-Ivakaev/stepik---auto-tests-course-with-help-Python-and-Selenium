from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def browser():
    print("\nOpen browser")
    browser = webdriver.Chrome()
    yield browser
    print("\n Close browser")
    time.sleep(3)
    browser.quit()


class TestNew():

    def test_quest1(self, browser):
        browser.get('http://stepik.org/lesson/236895/step/1')
        time.sleep(3)
        input1 = browser.find_element_by_tag_name("textarea")
        answer = math.log(int(time.time()))
        input1.send_keys(str(answer))
        button = browser.find_element_by_css_selector("button.submit-submission").click()
        welcome_text_elt = browser.find_element_by_css_selector(".smart-hints__hint")
        welcome_text = welcome_text_elt.text
        #self.assertEqual("Correct!", welcome_text)
        assert welcome_text == 'Correct!'
        
    @pytest.mark.skip
    def test_quest2(self, browser):
        browser.get("https://stepik.org/lesson/236896/step/1")
        time.sleep(3)
        input1 = browser.find_element_by_tag_name("textarea")
        answer = math.log(int(time.time()))
        input1.send_keys(str(answer))
        button = browser.find_element_by_css_selector("button.submit-submission").click()
    @pytest.mark.skip
    def test_quest3(self, browser):
        browser.get("https://stepik.org/lesson/236897/step/1")
        time.sleep(3)
        input1 = browser.find_element_by_tag_name("textarea")
        answer = math.log(int(time.time()))
        input1.send_keys(str(answer))
        button = browser.find_element_by_css_selector("button.submit-submission").click()
    @pytest.mark.skip
    def test_quest4(self, browser):
        browser.get("https://stepik.org/lesson/236898/step/1")
        time.sleep(3)
        input1 = browser.find_element_by_tag_name("textarea")
        answer = math.log(int(time.time()))
        input1.send_keys(str(answer))
        button = browser.find_element_by_css_selector("button.submit-submission").click()

    def test_quest5(self, browser):
        browser.get("https://stepik.org/lesson/236899/step/1")
        time.sleep(3)
        input1 = browser.find_element_by_tag_name("textarea")
        answer = math.log(int(time.time()))
        input1.send_keys(str(answer))
        button = browser.find_element_by_css_selector("button.submit-submission").click()
        #button = WebDriverWait(browser, 1).until(
         #   EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission")))
        welcome_text_elt = browser.find_element_by_css_selector(".smart-hints__hint")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Correct!", welcome_text)

    @pytest.mark.skip
    def test_quest6(self, browser):
        browser.get("https://stepik.org/lesson/236903/step/1")
        time.sleep(3)
        input1 = browser.find_element_by_tag_name("textarea")
        answer = math.log(int(time.time()))
        input1.send_keys(str(answer))
        button = browser.find_element_by_css_selector("button.submit-submission").click()
    @pytest.mark.skip
    def test_quest7(self, browser):
        browser.get("https://stepik.org/lesson/236904/step/1")
        time.sleep(3)
        input1 = browser.find_element_by_tag_name("textarea")
        answer = math.log(int(time.time()))
        input1.send_keys(str(answer))
        button = browser.find_element_by_css_selector("button.submit-submission").click()
    @pytest.mark.skip
    def test_quest8(self, browser):
        browser.get("https://stepik.org/lesson/236905/step/1")
        time.sleep(3)
        input1 = browser.find_element_by_tag_name("textarea")
        answer = math.log(int(time.time()))
        input1.send_keys(str(answer))
        button = browser.find_element_by_css_selector("button.submit-submission").click()
