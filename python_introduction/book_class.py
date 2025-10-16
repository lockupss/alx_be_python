class Book:
    """A simple Book class demonstrating Python magic methods."""

    def __init__(self, title: str, author: str, year: int):
        """Initialize a Book instance with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Called when the instance is about to be destroyed."""
        # Print deletion message using the book's title
        print(f"Deleting {self.title}")

    def __str__(self) -> str:
        """User-friendly string representation."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self) -> str:
        """Official string representation that can be used to recreate the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
