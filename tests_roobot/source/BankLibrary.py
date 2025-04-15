from bank_deposit1 import Bank_deposit


def create_bank_record():
    return Bank_deposit()


def register_client(bank, client_id, client_name):
    return bank.register_client(client_id, client_name)


def open_deposit_account(bank, client_id, start_balance, years, interest_frequency):
    return bank.open_deposit_account(client_id, start_balance, years, interest_frequency)


def calc_deposit_interest_rate(bank, client_id):
    return bank.calc_deposit_interest_rate(client_id)


def close_deposit(bank, client_id):
    return bank.close_deposit(client_id)
