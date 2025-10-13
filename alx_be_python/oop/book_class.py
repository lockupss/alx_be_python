"""Minimal Book class for ALX exercise (option A).

Provides a simple Book with title, author, pages, and methods
to read to a page, turn a page, bookmark current page, and
string representation.
"""

from __future__ import annotations


class Book:
    """A simple representation of a book.

    Attributes:
        title (str): Book title.
        author (str): Book author.
        pages (int): Number of pages in the book (must be > 0).
        current_page (int): Current page (0 means not started).
    """

    def __init__(self, title: str, author: str, pages: int):
        if not isinstance(title, str) or not isinstance(author, str):
            raise TypeError("title and author must be strings")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("pages must be a positive integer")

        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 0

    def read(self, page: int) -> None:
        """Set the current page while clamping to valid range.

        If the page provided is less than 0 it will be set to 0. If it is
        greater than the total number of pages it will be set to pages.
        """
        if not isinstance(page, int):
            raise TypeError("page must be an integer")

        if page < 0:
            self.current_page = 0
        elif page > self.pages:
            self.current_page = self.pages
        else:
            self.current_page = page

    def turn_page(self) -> None:
        """Advance one page if not at the end."""
        if self.current_page < self.pages:
            self.current_page += 1

    def bookmark(self) -> int:
        """Return the current page (simple bookmark)."""
        return self.current_page

    def __str__(self) -> str:
        return f"{self.title} by {self.author}"
