class Book:
    is_reserved = False
    is_given = False

    def __init__(self, book_name, author, num_pages, isbn):
        self.book_name = book_name
        self.author = author
        self.num_pages = num_pages
        self.isbn = isbn
        self.reserved_by = None
        self.given_to = None

    def __str__(self):
        return (f"Book name: '{self.book_name}', author: '{self.author}', "
                f"pages: {self.num_pages}, isbn: {self.isbn}")

    def reserve(self, reader_name):
        if Book.is_reserved:
            return False
        Book.is_reserved = True
        self.reserved_by = reader_name
        return True

    def cancel_reserve(self, reader_name):
        if not Book.is_reserved:
            return False
        if self.reserved_by == reader_name:
            Book.is_reserved = False
            self.reserved_by = None
            return True
        else:
            return False

    def get_book(self, reader_name):
        if Book.is_given:
            return False
        if Book.is_reserved:
            if self.reserved_by != reader_name:
                return False
        Book.is_given = True
        Book.is_reserved = False
        self.given_to = reader_name
        return True

    def return_book(self, reader_name):
        if not Book.is_given:
            return False
        if self.given_to == reader_name:
            Book.is_given = False
            self.given_to = None
            return True
        else:
            return False


class Reader:

    def __init__(self, name):
        self.name = name
        self.reserved_book = None
        self.given_book = None

    def __str__(self):
        return f"{self.name}"

    def reserve_book(self, book):
        if self.reserved_book is not None:
            return f"{book.isbn}: Warning! {self.name} already has a reserved book."
        if book.reserve(self.name):
            self.reserved_book = book
            return f"{book.isbn}: Success! Reservation for {self.name} is completed"
        else:
            return f"{book.isbn}: Warning! The book is already reserved by {book.reserved_by}"

    def cancel_reserve(self, book):
        if self.reserved_book is None:
            return f"{book.isbn}: Warning! {self.name} has no reservation for the book"
        if book.cancel_reserve(self.name):
            self.reserved_book = None
            return f"{book.isbn}: Success! Reservation for {self.name} is cancelled"
        else:
            return f"{book.isbn}: Warning! Reservation could not be cancelled"

    def get_book(self, book):
        if book.get_book(self.name):
            self.given_book = book
            return f"{book.isbn}: Success! The book is given to {self.name}"
        else:
            return f"{book.isbn}: Warning! The book cannot be given to {self.name}."

    def return_book(self, book):
        if book.return_book(self.name):
            self.given_book = None
            return f"{book.isbn}: Success! The book is returned by {self.name}"
        else:
            return f"{book.isbn}: Warning! The book could not be returned by {self.name}."


book1 = Book(book_name="The Hobbit", author="Books by J.R.R. Tolkien",
            num_pages=400, isbn="0006754023")
print(book1)

vasya = Reader("Vasya")
petya = Reader("Petya")

print(vasya.reserve_book(book1))
print(petya.reserve_book(book1))
print(vasya.reserve_book(book1))
print()
print(petya.cancel_reserve(book1))
print(vasya.cancel_reserve(book1))
print(vasya.cancel_reserve(book1))
print()
print(vasya.reserve_book(book1))
print()
print(petya.get_book(book1))
print(vasya.get_book(book1))
print(vasya.get_book(book1))
print()
print(petya.reserve_book(book1))
print(petya.get_book(book1))
print()
print(petya.return_book(book1))
print(vasya.return_book(book1))
print(vasya.return_book(book1))
