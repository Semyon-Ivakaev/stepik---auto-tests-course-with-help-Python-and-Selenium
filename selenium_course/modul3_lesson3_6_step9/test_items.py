import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    y = browser.find_element_by_css_selector("#add_to_basket_form button")
    time.sleep(3)
    assert y == browser.find_element_by_css_selector("#add_to_basket_form button"), \
           f"Button is false"
    
