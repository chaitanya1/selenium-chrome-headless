import unittest
from selenium import webdriver
from unittest.suite import TestSuite
from selenium.common.exceptions import NoSuchElementException

class duckduckgo(unittest.TestCase):
    """Include test cases on a given url"""

    def setUp(self):
        """Start web driver"""
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        """Stop web driver"""
        self.driver.quit()

    def test_case_1(self):
        """Opening Browser and navigating to search engine"""
        try:
            self.driver.get('https://duckduckgo.com')
            search_form = self.driver.find_element_by_id('search_form_input_homepage')
            search_form.send_keys('real python')
            search_form.submit()
            results = self.driver.find_elements_by_class_name('result')
            print(results[0].text)

        except NoSuchElementException as ex:
            self.fail(ex.msg)

if __name__ == '__main__':  
	# create the suite from the test classes
    suite = TestSuite()
    # load the tests
    tests = unittest.TestLoader()

	# add the tests to the suite
    suite.addTests(tests.loadTestsFromTestCase(duckduckgo))

    # run the suite
    runner = unittest.TextTestRunner()
    runner.run(suite)
