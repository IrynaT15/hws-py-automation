class Book:

    def __init__(self, book_name, author, num_pages, isbn):
        self.book_info = {
            "book_name" : book_name,
            "author" : author,
            "num_pages" : num_pages,
            "isbn" : isbn
        }

        self.status = {
            "is_reserved" : False,
            "is_given" : False,
            "reserved_by" : None,
            "given_to" : None
        }

    def __str__(self):
        return (f"Book name: '{self.book_info["book_name"]}',"
                f"author: '{self.book_info["author"]}',"
                f"pages: {self.book_info["num_pages"]},"
                f"isbn: {self.book_info["isbn"]}")

    def reserve(self, reader_name):
        if self.status["is_reserved"]:
            return False
        self.status["is_reserved"] = True
        self.status["reserved_by"] = reader_name
        return True

    def cancel_reserve(self, reader_name):
        if not self.status["is_reserved"]:
            return False
        if self.status["reserved_by"] == reader_name:
            self.status["is_reserved"] = False
            self.status["reserved_by"] = None
            return True
        else:
            return False

    def get_book(self, reader_name):
        if  self.status["is_given"]:
            return False
        if self.status["is_reserved"]:
            if self.status["reserved_by"] != reader_name:
                return False
        self.status["is_given"] = True
        self.status["is_reserved"] = False
        self.status["is_given"] = reader_name
        return True

    def return_book(self, reader_name):
        if not self.status["is_given"]:
            return False
        if self.status["given_to"] == reader_name:
            self.status["is_given"] = False
            self.status["given_to"] = None
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
            return f"{book.book_info['isbn']}: Warning! {self.name} already has a reserved book."
        if book.reserve(self.name):
            self.reserved_book = book
            return f"{book.book_info['isbn']}: Success! Reservation for {self.name} is completed"
        else:
            return (f"{book.book_info['isbn']}: Warning! The book is already reserved by"
                    f"{book.status['reserved_by']}")

    def cancel_reserve(self, book):
        if self.reserved_book is None:
            return f"{book.book_info['isbn']}: Warning! {self.name} has no reservation for the book"
        if book.cancel_reserve(self.name):
            self.reserved_book = None
            return f"{book.book_info['isbn']}: Success! Reservation for {self.name} is cancelled"
        else:
            return f"{book.book_info['isbn']}: Warning! Reservation could not be cancelled"

    def get_book(self, book):
        if book.get_book(self.name):
            self.given_book = book
            return f"{book.book_info['isbn']}: Success! The book can be given to {self.name}"
        else:
            return f"{book.book_info['isbn']}: Warning! The book cannot be given to {self.name}."

    def return_book(self, book):
        if book.return_book(self.name):
            self.given_book = None
            return f"{book.book_info['isbn']}: Success! The book is returned by {self.name}"
        else:
            return f"{book.book_info['isbn']}: Warning! The book could not be returned by {self.name}."


book = Book(book_name="The Hobbit", author="Books by J.R.R. Tolkien", num_pages=400, isbn="0006754023")
print(book)
book1 = Book(book_name="The Hobbit", author="Books by J.R.R. Tolkien", num_pages=400, isbn="00067540")
print(book)


vasya = Reader("Vasya")
petya = Reader("Petya")

print(vasya.reserve_book(book))
print(vasya.reserve_book(book))
print(petya.reserve_book(book))
print(vasya.cancel_reserve(book))
print(petya.reserve_book(book))
print(vasya.reserve_book(book))
print(vasya.get_book(book))
print(petya.get_book(book))
print(vasya.return_book(book))
print(petya.return_book(book))
print(vasya.get_book(book))
