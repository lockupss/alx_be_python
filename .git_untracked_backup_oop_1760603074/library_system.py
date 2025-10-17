class Book:
    """Base Book class with title and author."""

    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author


class EBook(Book):
    """EBook inherits from Book and adds file_size."""

    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size


class PrintBook(Book):
    """PrintBook inherits from Book and adds page_count."""

    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count


class Library:
    """A simple library that composes Book instances."""

    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        """Add a Book (or subclass) instance to the library."""
        if not isinstance(book, Book):
            raise TypeError("Only Book instances can be added to the library")
        self.books.append(book)

    def list_books(self):
        """Print details for each book in the library."""
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:
                print(f"Book: {book.title} by {book.author}")
