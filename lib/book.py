#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, page_count):
        if isinstance(page_count, int):
            self._page_count = page_count

        else:
            raise ValueError("page_count must be an integer")

    # Method for book => turn_page()
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

# Input calls - outside of class
input_title = input("Enter the Book Title: ")
input_page_count = input("Enter number of pages: ")

# Converting page_count to int
try:
    book = Book(input_title, int(input_page_count))
    print(f"Your added book is: \n {book.title} - {book.page_count}")
    book.turn_page()

except ValueError:
    raise ValueError ("page_count must be an integer")






