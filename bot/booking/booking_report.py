"""
This file includes method that will parse data we need from the first 20 book boxes
This file will run after filtration
"""
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By as BY

class BookingReport:
    def __init__(self, driver:WebDriver, boxes_section_element:WebElement):
        self.driver = driver
        self.boxes_section_element = boxes_section_element
        self.book_boxes = self.pull_book_boxes()
        
    def pull_book_boxes(self):
        return self.boxes_section_element.find_elements(
            BY.CLASS_NAME, 
            'searchResultItem'
            )
        
    def pull_book_details(self):
        collection = []
        for book_box in self.book_boxes:
            # pulling book titles
            title_element = book_box.find_element(
                BY.CLASS_NAME, 
                'booktitle'
                )
            book_title = title_element.text.strip()
            
            # pulling book authors
            author_element = book_box.find_element(
                BY.CLASS_NAME, 
                'bookauthor'
                )
            book_author = author_element.text.strip()
            
            # pulling ratings value
            rating_element = book_box.find_element(
                BY.CLASS_NAME, 
                'ratingsByline'
                )
            rating_value = rating_element.text.strip()
            
            collection.append([book_title, book_author, rating_value])
            
        return collection
        
            
            
        