import unittest
from selenium import webdriver
from pages.register import RegisterPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class EdxRegister(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.register = RegisterPage(self.driver)

    def test_register(self):
        self.driver.get('https://courses.stage.edx.org/register')
        self.assertTrue(self.register.is_browser_on_the_page())
        self.register.fill_form()
        self.register.submit_form()
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'a.btn.btn-primary')))
        browser_current_url = self.driver.current_url
        self.assertEqual(browser_current_url, 'https://courses.stage.edx.org/dashboard')

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
