from oop.book_class import Book


def test_book_init():
    b = Book("1984", "Orwell", 328, year=1949)
    assert b.title == "1984"
    assert b.author == "Orwell"
    assert b.pages == 328
    assert b.current_page == 0
    assert b.year == 1949


def test_read_and_bookmark():
    b = Book("Test", "Me", 10)
    b.read(5)
    assert b.current_page == 5
    assert b.bookmark() == 5


def test_turn_page_and_bounds():
    b = Book("Test", "Me", 3)
    b.read(2)
    b.turn_page()
    assert b.current_page == 3
    b.turn_page()
    assert b.current_page == 3  # doesn't go past end


def test_read_out_of_range():
    b = Book("Test", "Me", 7)
    b.read(999)
    assert b.current_page == 7
    b.read(-5)
    assert b.current_page == 0


def test_magic_methods_and_equality():
    b1 = Book("Dune", "Herbert", 412, year=1965)
    b2 = Book("Dune", "Herbert", 412, year=1965)
    b3 = Book("Dune", "Herbert", 412, year=1966)

    assert str(b1) == "Dune by Herbert"
    assert repr(b1).startswith("Book(title='Dune'") or repr(b1).startswith('Book(title="Dune"')
    assert b1 == b2
    assert not (b1 == b3)
    s = {b1, b2}
    assert len(s) == 1
