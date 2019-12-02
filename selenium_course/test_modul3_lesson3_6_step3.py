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
    browser.implicitly_wait(5)
    yield browser
    print("\n Close browser")
    browser.quit()

@pytest.mark.parametrize('value_link', ['236895', '236896', '236897',
                                        '236898', '236899', '236903',
                                        '236904', '236905'])
def test_see_link(browser, value_link):
    link = f"https://stepik.org/lesson/{value_link}/step/1"
    browser.get(link)
    input1 = browser.find_element_by_tag_name("textarea")
    answer = math.log(int(time.time()))
    input1.send_keys(str(answer))
    button = browser.find_element_by_css_selector("button.submit-submission").click()
    welcome_text_elt = browser.find_element_by_class_name("smart-hints__hint")
    welcome_text = welcome_text_elt.text
    assert welcome_text == 'Correct!', \
           f"This text is {welcome_text}"
