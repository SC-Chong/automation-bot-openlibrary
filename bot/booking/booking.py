import booking.constants as const
from selenium import webdriver
from selenium.webdriver.common.by import By as BY
from booking.booking_filtration import BookingFiltration
from booking.booking_report import BookingReport

class Booking(webdriver.Chrome):
    def __init__(self, teardown=False):
        self.teardown = teardown
        super(Booking, self).__init__() #instantiate instance of webdriver
        self.implicitly_wait(15) #wait 15 seconds max
        self.maximize_window()
        
    def __exit__(self, exc_type, exc, traceback):
        if self.teardown:
            self.quit()
        
    def land_first_page(self):
        self.get(const.BASE_URL)
        
    def change_language(self, language='English'):
        language_element = self.find_element(
            BY.CLASS_NAME, 
            'language-component'
            )
        language_element.click()
        try:
            selected_language_element = self.find_element(
                BY.CSS_SELECTOR,
                f'a[title={language}]'
                )
            selected_language_element.click()
        except:
            selected_language_element = self.find_element(
                BY.CSS_SELECTOR,
                'a[title="English"]' #if language not found, default English
                )
            print('Language not found, defaulting to English.')
            selected_language_element.click()
        
    def search_books(self, book_to_search):
        search_field = self.find_element(
            BY.CSS_SELECTOR,
            'input[aria-label="Search"]'
            )
        search_field.clear()
        search_field.send_keys(book_to_search)
 
    def click_search(self):
        search_button = self.find_element(
            BY.CSS_SELECTOR,
            'input[aria-label="Search submit"]'
            )
        search_button.click()
        
    def apply_filtrations(self, language_chosen=None):
        filtration = BookingFiltration(driver=self)
        filtration.apply_book_language(language_chosen=language_chosen)
        
    def report_results(self):
        book_boxes = self.find_element(
            BY.CLASS_NAME, 
            'list-books'
            )
                
        report = BookingReport(driver=self, boxes_section_element=book_boxes)
        books_table = report.pull_book_details()
        print(books_table)
        
        
        
        
                
        
        
        