"""Minimal Book class for ALX exercise (option A).

Provides a simple Book with title, author, pages, and methods
to read to a page, turn a page, bookmark current page, and
string representation.
"""

from __future__ import annotations


from typing import Optional


class Book:
    """A simple representation of a book.

    Attributes:
        title (str): Book title.
        author (str): Book author.
        pages (int): Number of pages in the book (must be > 0).
        current_page (int): Current page (0 means not started).
    """

    def __init__(self, title: str, author: str, pages: int, year: Optional[int] = None):
        if not isinstance(title, str) or not isinstance(author, str):
            raise TypeError("title and author must be strings")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("pages must be a positive integer")
        if year is not None and (not isinstance(year, int) or year <= 0):
            raise ValueError("year must be a positive integer when provided")

        self.title = title
        self.author = author
        self.pages = pages
        self.year = year
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

    def __repr__(self) -> str:  # readable representation for debugging
        return (
            f"Book(title={self.title!r}, author={self.author!r}, "
            f"pages={self.pages!r}, year={self.year!r})"
        )

    def __del__(self) -> None:
        """Destructor: clear references to help with deterministic cleanup.

        Note: __del__ is not guaranteed to be called at interpreter shutdown
        or if there are reference cycles. We keep it simple and safe.
        """
        try:
            # clear attributes to break potential reference cycles
            self.title = None  # type: ignore
            self.author = None  # type: ignore
            self.pages = None  # type: ignore
            self.year = None  # type: ignore
            self.current_page = None  # type: ignore
        except Exception:
            # avoid raising in destructor
            pass

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Book):
            return NotImplemented
        return (
            self.title == other.title
            and self.author == other.author
            and self.pages == other.pages
            and self.year == other.year
        )

    def __hash__(self) -> int:
        return hash((self.title, self.author, self.pages, self.year))
