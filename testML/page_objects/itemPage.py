from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class item():

    def __init__(self, my_driver):
        self.driver = my_driver
        self.add_cart = (By.XPATH, '//span[contains(text(),"Agregar al carrito")]')

    def select_add(self):
        self.driver.execute_script("window.scrollTo(0,600)")
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.add_cart)).click()