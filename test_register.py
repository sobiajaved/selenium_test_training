import unittest
from selenium import webdriver
from pages.register import RegisterPage


class EdxRegister(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.register = RegisterPage(self.driver)

    def test_register(self):
        self.driver.get('https://courses.stage.edx.org/register')
        self.assertTrue(self.register.is_browser_on_the_page())
        self.register.fill_form()
        self.register.submit_form()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
