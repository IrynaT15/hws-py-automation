from library1 import Reader


def create_reader(name):
    return Reader(name)


def reader_reserve_book(reader, book):
    return reader.reserve_book(book)


def reader_cancel_reserve(reader, book):
    return reader.cancel_reserve(book)


def reader_get_book(reader, book):
    return reader.get_book(book)


def reader_return_book(reader, book):
    return reader.return_book(book)
