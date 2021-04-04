from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

class items():

    def __init__(self, my_driver):
        self.driver = my_driver
        self.text_result = (By.XPATH, '//h1[@class="ui-search-breadcrumb__title"]')
        self.select_delivery = (By.XPATH, '//span[contains(text(),"Gratis")]')
        self.print = (By.XPATH, '//span[@class="ui-search-search-result__quantity-results"]')
        self.select = (By.XPATH, '//button[@class="andes-dropdown__trigger"]')
        self.sort_price = (By.XPATH, '//li[@value="price_desc"]')

    def search_result(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.text_result)).text

    def select_free_delivery(self):
        self.driver.execute_script("window.scrollTo(0,400)")
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.select_delivery)).click()
    
    def print_quantity_of_results(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.print)).text

    def sort(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.select)).click()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.sort_price)).click()
