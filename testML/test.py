import unittest
from selenium import webdriver
import time
from page_objects.indexPage import index
from page_objects.itemsPage import items
from page_objects.itemPage import item
from selenium.webdriver.chrome.options import Options

class Test(unittest.TestCase):

    def setUp(self):
        option = Options()
        option.add_argument('start-maximized')
        #option.add_argument('--headless')
        self.driver = webdriver.Chrome('testML/driver/chromedriver.exe', chrome_options=option)
        self.driver.get('https://www.mercadolibre.com.ar/')
        self.driver.implicitly_wait(5)
        self.index = index(self.driver)
        self.items = items(self.driver)
        self.item = item(self.driver)

    @unittest.skip('bla')
    def test_1_search(self):
        self.index.search_item('leatherman surge')
        self.assertEqual(self.items.search_result(), 'Leatherman surge')

    @unittest.skip('bla')
    def test_2_select_delivey(self):
        self.index.search_item('leatherman surge')
        self.items.select_free_delivery()
        self.assertEqual(self.items.assert_delivery(), 'Envío gratis')

    @unittest.skip('bla')
    def test_3_print_quantity(self):
        self.index.search_item('leatherman surge')
        self.items.select_free_delivery()
        self.items.print_quantity_of_results()

    @unittest.skip('bla')
    def test_4_sort_and_print(self):
        self.index.search_item('leatherman surge')
        self.items.select_free_delivery()
        self.items.print_quantity_of_results()
        self.items.sort()
        self.items.print_title_and_price(5)

    @unittest.skip('bla')
    def test_5_assert_tool(self):
        self.index.search_item('leatherman surge')
        self.items.select_free_delivery()
        self.items.print_quantity_of_results()
        self.items.sort()
        self.items.print_title_and_price(5)
        self.items.select_tool(0)
        self.items.assert_tool()

    #@unittest.skip('bla')
    def test(self):
        self.index.search_item('leatherman surge')
        self.items.select_free_delivery()
        self.items.print_quantity_of_results()
        self.items.sort()
        self.items.print_title_and_price(5)
        self.items.select_tool(0)
        self.item.select_add()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
