from library1 import Book


def create_book(book_name, author, num_pages, isbn):
    return Book(book_name, author, num_pages, isbn)


def reserve_book(book, reader_name):
    return book.reserve(reader_name)


def cancel_reserve(book, reader_name):
    return book.cancel_reserve(reader_name)


def get_book(book, reader_name):
    return book.get_book(reader_name)


def return_book(book, reader_name):
    return book.return_book(reader_name)
