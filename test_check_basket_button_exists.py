import time
from selenium.webdriver.common.by import By
def test_check_basket_button_exists(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/') 
    button_check = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket").is_displayed()
    assert button_check, "No money, no honey"
    time.sleep(3)