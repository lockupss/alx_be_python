from book_class import Book
import gc

def main():
    b = Book('1984', 'George Orwell', 328, year=1949)
    # Print exactly the expected lines (no extra prefixes)
    print(str(b))
    print(repr(b))
    # Delete to trigger __del__ message
    del b
    # Force garbage collection to encourage __del__ execution
    gc.collect()

if __name__ == '__main__':
    main()
