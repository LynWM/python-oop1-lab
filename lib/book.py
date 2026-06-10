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
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")


if __name__ == "__main__":
    input_title = input("Enter the Book Title: ")
    input_page_count = input("Enter number of pages: ")

    try:
        book = Book(input_title, int(input_page_count))
        print(f"Title: {book.title}, Pages: {book.page_count}")
        book.turn_page()
    except ValueError:
        print("page_count must be an integer")