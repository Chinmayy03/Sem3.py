class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(book, "added successfully")

    def display_books(self):
        print("Available Books:")
        for book in self.books:
            print(book)


library = Library()
library.add_book("Python Programming")
library.add_book("Java Programming")
library.add_book("Data Structures")
library.display_books()
