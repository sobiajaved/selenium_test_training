from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random

class RegisterPage(object):

    def __init__(self, driver):
        self.driver = driver

    def is_browser_on_the_page(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.action.action-primary.action-update.js-register.register-button')))
        return True

    def randmfuntest(self):
        first_name = ['abc', 'aac', 'aaa', 'asa', 'qwe', 'wwd', 'asg']
        last_name = ['atbc', 'uaac', 'jaaa', 'oasa', 'dqwe', 'ewwd', 'aksg']
        for num in range(50):
            first = random.choice(first_name)
            last = random.choice(last_name)
            email = first.lower() + last.lower() + '@test.com'
            return email


    def fill_form(self):
        email = self.randmfuntest()
        email_elem = self.driver.find_element_by_css_selector('#register-email')
        email_elem.send_keys(email)
        name_elem = self.driver.find_element_by_css_selector('#register-name')
        name_elem.send_keys('sss')
        rname_elem = self.driver.find_element_by_css_selector('#register-username')
        rname_elem.send_keys('sssaaaafff')
        pwd_elem = self.driver.find_element_by_css_selector('#register-password')
        pwd_elem.send_keys('1234567a')
        select_elem = Select(self.driver.find_element_by_css_selector('#register-country'))
        select_elem.select_by_visible_text('Pakistan')

    def submit_form(self):
        create_account = self.driver.find_element_by_css_selector('button.action.action-primary.action-update.js-register.register-button')
        create_account.click()