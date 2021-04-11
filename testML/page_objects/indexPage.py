from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class index:

    def __init__(self, my_driver):
        self.driver = my_driver
        self.query_search = (By.XPATH, '//input[@class="nav-search-input"]')
        self.button_search = (By.XPATH, '//div[@class="nav-icon-search"]')

    def search_item(self, item):
        search = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.query_search)).send_keys(item)
        find = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.button_search)).click()
