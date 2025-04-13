import unittest
from bank_deposit import Bank_deposit


class TestBankDeposit(unittest.TestCase):

    def setUp(self):
        self.bank1 = Bank_deposit()
        self.bank1.register_client("001", "Name1")

    def tearDown(self):
        Bank_deposit.clients_ids = []

    def test_register_client_success(self):
        self.assertEqual(self.bank1.client_id, "001")
        self.assertEqual(self.bank1.client_name, "Name1")

    def test_register_client_fail_existing_client_id(self):
        self.assertIn("Warning", self.bank1.register_client("001", "Name2"))

    def test_open_deposit_account_success(self):
        self.assertIn("Success", self.bank1.open_deposit_account("001", 1000, 5, 12))
        self.assertEqual(self.bank1.start_balance, 1000)
        self.assertEqual(self.bank1.years, 5)
        self.assertEqual(self.bank1.interest_frequency, 12)
        self.assertTrue(self.bank1.is_deposit_open)

    def test_open_deposit_account_fail_not_registered_client(self):
        self.assertIn("Warning", self.bank1.open_deposit_account("002", 1000, 5, 12))

    def test_open_deposit_account_fail_client_already_has_deposit(self):
        self.bank1.open_deposit_account("001", 1000, 5, 12)
        self.assertIn("Warning", self.bank1.open_deposit_account("001", 2000, 10, 12))

    def test_open_deposit_account_fail_negative_balance(self):
        self.assertIn("Warning", self.bank1.open_deposit_account("001", -100, 1, 12))

    def test_open_deposit_account_fail_zero_balance(self):
        self.assertIn("Warning", self.bank1.open_deposit_account("001", 0, 1, 12))

    def test_calc_deposit_interest_rate_success(self):
        self.bank1.open_deposit_account("001", 1000, 1, 12)
        self.assertEqual(self.bank1.calc_deposit_interest_rate("001"), 1104.71)

    def test_close_deposit_success(self):
        self.bank1.open_deposit_account("001", 1000, 1, 12)
        self.assertIn("Success", self.bank1.close_deposit("001"))
        self.assertEqual(self.bank1.start_balance, 0)
        self.assertEqual(self.bank1.years, 0)
        self.assertEqual(self.bank1.interest_frequency, 0)
        self.assertFalse(self.bank1.is_deposit_open)

    def test_close_deposit_fail_not_registered_client(self):
        self.assertIn("Warning", self.bank1.close_deposit("002"))


if __name__ == "__main__":
    unittest.main()
