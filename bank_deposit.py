class Bank_deposit:
    interest_rate = 0.1
    clients_ids = []

    def __init__(self):
        self.client_id = None
        self.client_name = None
        self.is_deposit_open = False
        self.start_balance = None
        self.years = None
        self.interest_frequency = None

    def register_client(self, client_id, client_name):
        if client_id in Bank_deposit.clients_ids:
            return f"{client_id}: Warning! Client is already registered"
        self.client_id = client_id
        self.client_name = client_name
        Bank_deposit.clients_ids.append(self.client_id)
        return f"{self.client_id}: Success! New client is registered"

    def open_deposit_account(self, client_id, start_balance, years, interest_frequency):
        self.client_id = client_id
        if self.client_id not in Bank_deposit.clients_ids:
            return "Warning! Client not registered."
        if self.is_deposit_open:
            return f"{self.client_id}: Warning! Client has an open deposit."
        self.start_balance = start_balance
        self.years = years
        self.interest_frequency = interest_frequency
        self.is_deposit_open = True
        return f"{self.client_id}: Success! Deposit account is opened. {self.start_balance} BYN for {self.years} years."

    def calc_deposit_interest_rate(self, client_id):
        self.client_id = client_id
        if self.client_id not in Bank_deposit.clients_ids:
            return "Warning! Client not registered."
        if not self.is_deposit_open:
            return f"{self.client_id}: Warning! No open deposit account."
        final_balance = self.start_balance * ((1 + Bank_deposit.interest_rate / self.interest_frequency) ** (self.interest_frequency * self.years))
        return f"Final balance: {round(final_balance, 2)}"

    def close_deposit(self, client_id):
        self.client_id = client_id
        if self.client_id not in Bank_deposit.clients_ids:
            return "Warning! Client not registered."
        self.start_balance = 0
        self.years = 0
        self.interest_frequency = 0
        self.is_deposit_open = False
        return f"{self.client_id}: Success! Deposit account is closed"


bank = Bank_deposit()
print(bank.register_client("0000001", "Iryna Tain"))
print(bank.open_deposit_account("0000002", 1000, 1, 12))
print(bank.open_deposit_account("0000001", 1000, 1, 12))
print(bank.calc_deposit_interest_rate("0000001"))
print(bank.close_deposit("0000001"))
print(bank.register_client("0000001", "Iryna Tain"))
