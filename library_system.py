# library_system.py

class Book:
    """Base class representing a book"""
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class representing an electronic book"""
    
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size
    
    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class representing a physical printed book"""
    
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count
    
    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Class demonstrating composition by managing a collection of books"""
    
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        """Add a Book, EBook, or PrintBook instance to the library"""
        self.books.append(book)
    
    def list_books(self):
        """Print details of each book in the library"""
        for book in self.books:
            print(book)
