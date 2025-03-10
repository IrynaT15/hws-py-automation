import json

class Currency:

    def __init__(self, rates_file):
        self.rates_file = rates_file

    def __str__(self):
        return f"{self.get_currency_rate()}"

    def get_currency_rate(self):
        with open(self.rates_file) as working_file:
            working_data = json.load(working_file)
        return working_data


class CurrencyConverter(Currency):

    def __init__(self, rates_file):
        super().__init__(rates_file)
        self.rates_data = self.get_currency_rate()

    def exchange_currency(self, currency_from, amount, currency_to = "BYN"):

        if currency_from not in self.rates_data["currency_code"]:
            return f"The converter does not support {currency_from}"
        if currency_to not in self.rates_data["currency_code"]:
            return f"The converter does not support {currency_to}"

        if currency_from == "BYN":
            rate_data = self.rates_data["currency_rate_byn"]
        elif currency_from == "EUR":
            rate_data = self.rates_data["currency_rate_eur"]
        elif currency_from == "USD":
            rate_data = self.rates_data["currency_rate_usd"]

        rate = rate_data[currency_to]
        converted_amount = round(amount * rate, 2)

        return converted_amount, currency_to


class Person:

    def __init__(self, currency_from, amount):
        self.currency_from = currency_from
        self.amount = amount

    def __str__(self):
        return f"Convert {self.amount} {self.currency_from}"



cur = Currency("currency_rates.json")
print(cur)
vasya = Person('EUR', 10)
print(vasya)
converter = CurrencyConverter("currency_rates.json")
print(converter.exchange_currency(vasya.currency_from, vasya.amount, "USD"))
