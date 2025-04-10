import pytest
from library import Book, Reader


class TestBook:
    @pytest.fixture(autouse=True)
    def create_book(self):
        self.book = Book(
            book_name="The Hobbit",
            author="Books by J.R.R. Tolkien",
            num_pages=400,
            isbn="0006754023"
        )

    def test_reserve_book_success(self, configure_logger):
        logger = configure_logger
        assert self.book.reserve("Reader 1") is True
        logger.info("Book is reserved successfully by Reader 1")
        assert self.book.status["is_reserved"] is True
        assert self.book.status["reserved_by"] == "Reader 1"
        logger.info(f"Book status: {self.book.status}")

    def test_reserve_book_fail_already_reserved(self, configure_logger):
        logger = configure_logger
        self.book.reserve("Reader 1")
        assert self.book.reserve("Reader 1") is False
        logger.warning("Book reservation fails. Reason: book is already reserved.")

    def test_cancel_reservation_success(self, configure_logger):
        logger = configure_logger
        self.book.reserve("Reader 1")
        assert self.book.cancel_reserve("Reader 1") is True
        logger.info("Book reservation by Reader 1 is cancelled.")
        assert self.book.status["is_reserved"] is False
        assert self.book.status["reserved_by"] is None
        logger.info(f"Book status: {self.book.status}")

    def test_cancel_reservation_fail_wrong_reader(self, configure_logger):
        logger = configure_logger
        self.book.reserve("Reader 1")
        assert self.book.cancel_reserve("Reader 2") is False
        logger.warning("Cancellation of book reservation fails. "
                       "Reason: book is reserved by Reader 1. Reader 2 is cancelling.")

    def test_get_reserved_book_success(self, configure_logger):
        logger = configure_logger
        self.book.reserve("Reader 1")
        assert self.book.get_book("Reader 1") is True
        logger.info("Reserved book is given to Reader 1.")
        assert self.book.status["is_given"] is True
        assert self.book.status["is_reserved"] is False
        assert self.book.status["given_to"] == "Reader 1"
        logger.info(f"Book status: {self.book.status}")

    def test_get_not_reserved_book_success(self, configure_logger):
        logger = configure_logger
        assert self.book.get_book("Reader 1") is True
        logger.info("Non-reserved book is given to Reader 1.")
        assert self.book.status["is_given"] is True
        assert self.book.status["is_reserved"] is False
        assert self.book.status["given_to"] == "Reader 1"
        logger.info(f"Book status: {self.book.status}")

    def test_get_book_fail_reserved_by_another_reader(self, configure_logger):
        logger = configure_logger
        self.book.reserve("Reader 1")
        assert self.book.get_book("Reader 2") is False
        logger.warning("Book cannot be given to Reader 2. "
                       "Reason: book is reserved by Reader 1.")

    def test_get_book_fail_already_given(self, configure_logger):
        logger = configure_logger
        self.book.get_book("Reader 1")
        assert self.book.get_book("Reader 1") is False
        logger.warning("Book cannot be given to Reader 1. "
                       "Reason: book is already given to Reader 1.")

    def test_return_book_success(self, configure_logger):
        logger = configure_logger
        self.book.get_book("Reader 1")
        assert self.book.return_book("Reader 1") is True
        logger.info("Book is returned successfully by Reader 1.")
        assert self.book.status["is_given"] is False
        assert self.book.status["given_to"] is None
        logger.info(f"Book status: {self.book.status}")

    def test_return_book_fail_wrong_reader(self, configure_logger):
        logger = configure_logger
        self.book.get_book("Reader 1")
        assert self.book.return_book("Reader 2") is False
        logger.warning("Book cannot be returned by Reader 2. "
                       "Reason: wrong reader, book is given to Reader 1.")


class TestReader:
    @pytest.fixture(autouse=True)
    def create_reader(self):
        self.reader = Reader("Reader 1")

    @pytest.fixture(autouse=True)
    def create_book(self):
        self.book = Book(
            book_name="The Hobbit",
            author="Books by J.R.R. Tolkien",
            num_pages=400,
            isbn="0006754023"
        )

    @pytest.fixture
    def create_book_2(self):
        self.book_2 = Book(
            book_name="The Hobbit 2",
            author="Books by J.R.R. Tolkien",
            num_pages=300,
            isbn="0006754024"
        )

    def test_reader_reserve_book_success(self, configure_logger):
        logger = configure_logger
        assert self.reader.reserve_book(self.book) == ("0006754023: Success! "
                                                       "Reservation for Reader 1 is completed")
        logger.info(f"{self.reader.name} reserved a book: {self.book.book_info['book_name']}")
        assert self.reader.reserved_book == self.book

    def test_reader_cannot_reserve_second_book(self, create_book_2, configure_logger):
        logger = configure_logger
        self.reader.reserve_book(self.book)
        assert self.reader.reserve_book(self.book_2) == ("0006754024: Warning! "
                                                         "Reader 1 already has a reserved book")
        logger.warning(
            f"{self.reader.name} cannot reserve book {self.book.book_info['book_name']}. "
            f"Reason: {self.reader.name} already has "
            f"a reserved book: {self.book.book_info['book_name']}")

    def test_reader_reserve_book_fail_book_already_reserved(self, configure_logger):
        logger = configure_logger
        self.book.reserve("Reader 2")
        assert self.reader.reserve_book(self.book) == ("0006754023: Warning! "
                                                       "The book is already reserved by Reader 2")
        logger.warning(
            f"{self.reader.name} cannot reserve book {self.book.book_info['book_name']}. "
            f"Reason: Book is already reserved.")

    def test_reader_cancel_reservation_success(self, configure_logger):
        logger = configure_logger
        self.reader.reserve_book(self.book)
        assert self.reader.cancel_reserve(self.book) == ("0006754023: Success! "
                                                         "Reservation for Reader 1 is cancelled")
        logger.info(f"{self.reader.name} cancelled book reservation")
        assert self.reader.reserved_book is None

    def test_reader_cancel_reservation_fail_book_not_reserved_by_reader(self, configure_logger):
        logger = configure_logger
        self.book.reserve("Reader 2")
        assert self.reader.cancel_reserve(self.book) == ("0006754023: Warning! "
                                                         "Reader 1 has no reservation for the book")
        logger.warning(
            f"{self.reader.name} cannot cancel reservation."
            f"Reason: Book {self.book.book_info['book_name']} is not reserved.")

    def test_reader_get_reserved_book_success(self, configure_logger):
        logger = configure_logger
        self.reader.reserve_book(self.book)
        assert self.reader.get_book(self.book) == ("0006754023: Success! "
                                                   "The book can be given to Reader 1")
        logger.info(f"{self.reader.name} is given "
                    f"reserved book {self.book.book_info['book_name']}")
        assert self.reader.given_book == self.book

    def test_reader_get_not_reserved_book_success(self, configure_logger):
        logger = configure_logger
        assert self.reader.get_book(self.book) == ("0006754023: Success! "
                                                   "The book can be given to Reader 1")
        logger.info(f"{self.reader.name} is given "
                    f"non-reserved book {self.book.book_info['book_name']}")
        assert self.reader.given_book == self.book

    def test_reader_get_book_fail_reserved_by_another_reader(self, configure_logger):
        logger = configure_logger
        self.book.reserve("Reader 2")
        assert self.reader.get_book(self.book) == ("0006754023: Warning! "
                                                   "The book cannot be given to Reader 1")
        logger.warning(
            f"{self.reader.name} cannot get book."
            f"Reason: Book {self.book.book_info['book_name']} is reserved by another reader.")

    def test_reader_get_book_fail_already_given(self, configure_logger):
        logger = configure_logger
        self.book.get_book("Reader 2")
        assert self.reader.get_book(self.book) == ("0006754023: Warning! "
                                                   "The book cannot be given to Reader 1")
        logger.warning(
            f"{self.reader.name} cannot get book."
            f"Reason: Book {self.book.book_info['book_name']} is already given.")

    def test_reader_return_book_success(self, configure_logger):
        logger = configure_logger
        self.reader.get_book(self.book)
        assert self.reader.return_book(self.book) == ("0006754023: Success! "
                                                      "The book is returned by Reader 1")
        logger.info(f"{self.reader.name} returns "
                    f"book {self.book.book_info['book_name']} successfully.")
        assert self.reader.given_book is None

    def test_reader_return_book_fail_wrong_book(self, create_book_2, configure_logger):
        logger = configure_logger
        self.reader.get_book(self.book_2)
        assert self.reader.return_book(self.book) == ("0006754023: Warning! "
                                                      "The book could not be returned by Reader 1")
        logger.warning(
            f"{self.reader.name} cannot return book {self.book.book_info['book_name']}."
            f"Reason: Reader returns wrong book.")

    def test_reader_return_book_fail_book_not_given(self, configure_logger):
        logger = configure_logger
        assert self.reader.return_book(self.book) == ("0006754023: Warning! "
                                                      "The book could not be returned by Reader 1")
        logger.warning(
            f"{self.reader.name} cannot return book {self.book.book_info['book_name']}."
            f"Reason: Book was not given.")

    def test_reader_return_book_fail_book_already_returned(self, configure_logger):
        logger = configure_logger
        self.reader.get_book(self.book)
        self.reader.return_book(self.book)
        assert self.reader.return_book(self.book) == ("0006754023: Warning! "
                                                      "The book could not be returned by Reader 1")
        logger.warning(
            f"{self.reader.name} cannot return book {self.book.book_info['book_name']}."
            f"Reason: Book is already returned.")
