"""
This file includes a class with instance methods
This file will interact with website after having click search to apply filtration
"""
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By as BY

class BookingFiltration:
    def __init__(self, driver:WebDriver):
        self.driver = driver
        
    def apply_book_language(self, language_chosen=None):
        if language_chosen is not None:
            try:
                language_element = self.driver.find_element(
                    BY.CSS_SELECTOR,
                    f'a[title="Filter results for {language_chosen}"]'
                    )
                language_element.click()
            except:
                print("Book language input not applicable, skip filtering book language...")
                
    
        
