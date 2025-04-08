import unittest
from library import Book, Reader

class TestBook(unittest.TestCase):

    def setUp(self):
        self.book1 = Book(
            book_name="The Hobbit",
            author="Books by J.R.R. Tolkien",
            num_pages=400,
            isbn="0006754023"
        )

    def test_reserve_book_success(self):
        self.assertTrue(self.book1.reserve("Reader1"))
        self.assertTrue(self.book1.status["is_reserved"])
        self.assertEqual(self.book1.status["reserved_by"], "Reader1")

    def test_reserve_book_fail_already_reserved(self):
        self.book1.reserve("Reader1")
        self.assertFalse(self.book1.reserve("Reader2"))

    def test_cancel_reservation_success(self):
        self.book1.reserve("Reader1")
        self.assertTrue(self.book1.cancel_reserve("Reader1"))
        self.assertFalse(self.book1.status["is_reserved"])
        self.assertIsNone(self.book1.status["reserved_by"])

    def test_cancel_reservation_fail_wrong_reader(self):
        self.book1.reserve("Reader1")
        self.assertFalse(self.book1.cancel_reserve("Reader2"))

    def test_get_reserved_book_success(self):
        self.book1.reserve("Reader1")
        self.assertTrue(self.book1.get_book("Reader1"))
        self.assertTrue(self.book1.status["is_given"])
        self.assertFalse(self.book1.status["is_reserved"])
        self.assertEqual(self.book1.status["given_to"], "Reader1")

    def test_get_not_reserved_book_success(self):
        self.assertFalse(self.book1.status["is_reserved"])
        self.assertTrue(self.book1.get_book("Reader1"))
        self.assertTrue(self.book1.status["is_given"])
        self.assertFalse(self.book1.status["is_reserved"])
        self.assertEqual(self.book1.status["given_to"], "Reader1")

    def test_get_book_fail_reserved_by_another_reader(self):
        self.book1.reserve("Reader1")
        self.assertFalse(self.book1.get_book("Reader2"))

    def test_get_book_fail_already_given(self):
        self.book1.get_book("Reader1")
        self.assertFalse(self.book1.get_book("Reader2"))

    def test_return_book_success(self):
        self.book1.get_book("Reader1")
        self.assertTrue(self.book1.return_book("Reader1"))
        self.assertFalse(self.book1.status["is_given"])
        self.assertIsNone(self.book1.status["given_to"])

    def test_return_book_fail_wrong_reader(self):
        self.book1.get_book("Reader1")
        self.assertFalse(self.book1.return_book("Reader2"))


class TestReader(unittest.TestCase):

    def setUp(self):
        self.book1 = Book(
            book_name="The Hobbit",
            author="Books by J.R.R. Tolkien",
            num_pages=400,
            isbn="0006754023"
        )
        self.book2 = Book(
            book_name="The Hobbit - 2",
            author="Books by J.R.R. Tolkien",
            num_pages=300,
            isbn="0006754024"
        )
        self.reader1 = Reader("Reader1")
        self.reader2 = Reader("Reader2")

    def test_reader_reserve_book_success(self):
        self.assertIn("Success", self.reader1.reserve_book(self.book1))
        self.assertEqual(self.reader1.reserved_book, self.book1)

    def test_reader_cannot_reserve_second_book(self):
        self.reader1.reserve_book(self.book1)
        self.assertIn("Warning", self.reader1.reserve_book(self.book2))

    def test_reader_reserve_book_fail_book_already_reserved(self):
        self.reader1.reserve_book(self.book1)
        self.assertIn("Warning", self.reader2.reserve_book(self.book1))

    def test_another_reader_reserve_another_book_success(self):
        self.reader1.reserve_book(self.book1)
        self.assertIn("Success", self.reader2.reserve_book(self.book2))
        self.assertEqual(self.reader2.reserved_book, self.book2)

    def test_reader_cancel_reservation_success(self):
        self.reader1.reserve_book(self.book1)
        self.assertIn("Success", self.reader1.cancel_reserve(self.book1))
        self.assertIsNone(self.reader1.reserved_book)

    def test_reader_cancel_reservation_fail_book_not_reserved_by_reader(self):
        self.reader1.reserved_book = None
        self.assertIn("Warning", self.reader1.cancel_reserve(self.book1))

    def test_reader_cancel_reservation_fail_book_reserved_by_other_reader(self):
        self.reader1.reserve_book(self.book1)
        self.assertIn("Warning", self.reader2.cancel_reserve(self.book1))

    def test_reader_get_reserved_book_success(self):
        self.reader1.reserve_book(self.book1)
        self.assertIn("Success", self.reader1.get_book(self.book1))
        self.assertEqual(self.reader1.given_book, self.book1)

    def test_reader_get_not_reserved_book_success(self):
        self.book1.status["is_reserved"] = False
        self.assertIn("Success", self.reader1.get_book(self.book1))
        self.assertEqual(self.reader1.given_book, self.book1)

    def test_reader_get_book_fail_reserved_by_another_reader(self):
        self.reader1.reserve_book(self.book1)
        self.assertIn("Warning", self.reader2.get_book(self.book1))

    def test_reader_get_book_fail_already_given(self):
        self.book1.get_book(self.reader1)
        self.assertIn("Warning", self.reader2.get_book(self.book1))

    def test_reader_return_book_success(self):
        self.reader1.get_book(self.book1)
        self.assertIn("Success", self.reader1.return_book(self.book1))
        self.assertIsNone(self.reader1.given_book)

    def test_reader_return_book_fail_wrong_book(self):
        self.reader1.get_book(self.book1)
        self.assertIn("Warning", self.reader1.return_book(self.book2))

    def test_reader_return_book_fail_book_not_given(self):
        self.assertIn("Warning", self.reader1.return_book(self.book1))


if __name__ == "__main__":
    unittest.main()
