import unittest
from selenium import webdriver
import time
from indexPage import index
from itemsPage import items
from itemPage import item
from selenium.webdriver.chrome.options import Options

class Test(unittest.TestCase):

    def setUp(self):
        option = Options()
        option.add_argument('start-maximized')
        self.driver = webdriver.Chrome('chromedriver.exe', chrome_options=option)
        self.driver.get('https://www.mercadolibre.com.ar/')
        self.driver.implicitly_wait(5)
        self.index = index(self.driver)
        self.items = items(self.driver)
        self.item = item(self.driver)

    def test(self):
        self.index.search_item('leatherman surge')
        self.assertEqual(self.items.search_result(), 'Leatherman surge')
        self.items.select_free_delivery()
        print(self.items.print_results())
        self.items.sort()
        self.item.select_tool(0)
        self.item.select_add()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
