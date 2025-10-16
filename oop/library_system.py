"""Library system demonstrating inheritance and composition.

Classes:
- Book: base class with title and author.
- EBook: inherits Book, adds file_size (int, KB).
- PrintBook: inherits Book, adds page_count (int).
- Library: composition class holding a collection of books and providing
  methods to add and list books.

This file is placed in `oop/library_system.py` per exercise instructions.
"""

from typing import List


class Book:
    def __init__(self, title: str, author: str) -> None:
        if not isinstance(title, str) or not isinstance(author, str):
            raise TypeError("title and author must be strings")
        self.title = title
        self.author = author

    def details(self) -> str:
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int) -> None:
        super().__init__(title, author)
        if not isinstance(file_size, int) or file_size < 0:
            raise ValueError("file_size must be a non-negative integer")
        self.file_size = file_size

    def details(self) -> str:
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int) -> None:
        super().__init__(title, author)
        if not isinstance(page_count, int) or page_count < 0:
            raise ValueError("page_count must be a non-negative integer")
        self.page_count = page_count

    def details(self) -> str:
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self) -> None:
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        if not isinstance(book, Book):
            raise TypeError("book must be an instance of Book or its subclasses")
        self.books.append(book)

    def list_books(self) -> None:
        for b in self.books:
            print(b.details())
