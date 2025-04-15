class Bank_deposit:
    interest_rate = 0.1

    def __init__(self):
        self.client_ids = []
        self.client_id = None
        self.client_name = None
        self.is_deposit_open = False
        self.start_balance = None
        self.years = None
        self.interest_frequency = None

    def register_client(self, client_id, client_name):
        if client_id in self.client_ids:
            return f"{client_id}: Warning! Client is already registered"
        self.client_id = client_id
        self.client_name = client_name
        self.client_ids.append(self.client_id)
        return f"{self.client_id}: Success! New client is registered"

    def open_deposit_account(self, client_id, start_balance, years, interest_frequency):
        if client_id not in self.client_ids:
            return "Warning! Client not registered."
        if self.is_deposit_open:
            return f"{client_id}: Warning! Client has an open deposit."
        if int(start_balance) <= 0:
            return "Warning! Invalid start balance."
        self.start_balance = int(start_balance)
        self.years = int(years)
        self.interest_frequency = int(interest_frequency)
        self.is_deposit_open = True
        return (f"{client_id}: Success! Deposit account is opened. "
                f"{self.start_balance} BYN for {self.years} years.")

    def calc_deposit_interest_rate(self, client_id):
        if client_id not in self.client_ids:
            return "Warning! Client not registered."
        if not self.is_deposit_open:
            return f"{client_id}: Warning! No open deposit account."
        final_balance = self.start_balance * (
                (1 + Bank_deposit.interest_rate / self.interest_frequency) **
                (self.interest_frequency * self.years)
        )
        return round(final_balance, 2)

    def close_deposit(self, client_id):
        if client_id not in self.client_ids:
            return "Warning! Client not registered."
        if not self.is_deposit_open:
            return "Warning! Client has no open deposit account."
        self.start_balance = 0
        self.years = 0
        self.interest_frequency = 0
        self.is_deposit_open = False
        return f"{client_id}: Success! Deposit account is closed"
