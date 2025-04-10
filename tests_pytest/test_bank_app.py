import pytest
from bank_deposit import Bank_deposit


@pytest.fixture
def bank():
    return Bank_deposit()


@pytest.fixture
def client(bank):
    bank.register_client("001", "Name1")
    bank.client_id = "001"
    bank.client_name = "Name1"
    bank.clients_ids = ["001"]


@pytest.fixture
def deposit(bank):
    bank.open_deposit_account("001", 1000, 1, 12)
    bank.client_id = "001"
    bank.start_balance = 1000
    bank.years = 1
    bank.interest_frequency = 12
    bank.is_deposit_open = True


def test_register_client_success(bank, configure_logger):
    logger = configure_logger
    assert bank.register_client("001", "Name1") == "001: Success! New client is registered"
    assert bank.client_id == "001"
    assert bank.client_name == "Name1"
    assert "001" in bank.clients_ids
    logger.info(f"A new client is registered. "
                f"Client id: {bank.client_id}. Client name: {bank.client_name}")


def test_register_client_fail_existing_client_id(bank, client, configure_logger):
    logger = configure_logger
    assert bank.register_client("001", "Name1") == "001: Warning! Client is already registered"
    logger.warning(f"Warning! The client is not registered. "
                   f"Reason: Client id {bank.client_id} already exists.")


def test_open_deposit_account_success(bank, client, configure_logger):
    logger = configure_logger
    assert (bank.open_deposit_account("001", 1000, 5, 12) ==
            "001: Success! Deposit account is opened. 1000 BYN for 5 years.")
    assert bank.start_balance == 1000
    assert bank.years == 5
    assert bank.interest_frequency == 12
    assert bank.is_deposit_open is True
    logger.info(f"A registered client has opened a deposit. "
                f"Client id {bank.client_id}. "
                f"Start balance: {bank.start_balance}. "
                f"Years: {bank.years}. "
                f"Interest frequency: {bank.interest_frequency} months.")


def test_open_deposit_account_fail_not_registered_client(bank, client, configure_logger):
    logger = configure_logger
    assert (bank.open_deposit_account("01", 1000, 5, 12) ==
            "Warning! Client not registered.")
    logger.warning("Warning! A deposit is not opened. Reason: ClientId is not registered.")


def test_open_deposit_account_fail_client_already_has_deposit(
        bank, client, deposit, configure_logger):
    logger = configure_logger
    assert (bank.open_deposit_account("001", 2000, 10, 12) ==
            "001: Warning! Client has an open deposit.")
    logger.warning(f"Warning! A deposit is not opened. "
                   f"Reason: ClientId {bank.client_id} has an open deposit.")


def test_open_deposit_account_fail_negative_balance(bank, client, configure_logger):
    logger = configure_logger
    assert (bank.open_deposit_account("001", -100, 1, 12) ==
            "Warning! Invalid start balance.")
    assert bank.is_deposit_open is False
    logger.warning("Warning! A deposit is not opened. "
                   "Reason: Invalid start balance. Start balance: -100")


def test_open_deposit_account_fail_zero_balance(bank, client, configure_logger):
    logger = configure_logger
    assert (bank.open_deposit_account("001", 0, 1, 12) ==
            "Warning! Invalid start balance.")
    assert bank.is_deposit_open is False
    logger.warning("Warning! A deposit is not opened. "
                   "Reason: Invalid start balance. Start balance: 0")


def test_calc_deposit_interest_rate_success(bank, client, deposit, configure_logger):
    logger = configure_logger
    assert bank.calc_deposit_interest_rate("001") == 1104.71
    logger.info("Deposit interest rate is calculated.")


def test_calc_deposit_interest_rate_fail_no_open_deposit(bank, client, configure_logger):
    logger = configure_logger
    assert bank.calc_deposit_interest_rate("001") == "001: Warning! No open deposit account."
    logger.warning(f"Warning! ClientId {bank.client_id} has no deposit account.")


def test_close_deposit_success(bank, client, deposit, configure_logger):
    logger = configure_logger
    assert bank.close_deposit("001") == "001: Success! Deposit account is closed"
    assert bank.start_balance == 0
    assert bank.years == 0
    assert bank.interest_frequency == 0
    assert bank.is_deposit_open is False
    logger.info("Deposit account is closed.")


def test_close_deposit_fail_not_registered_client(bank, client, deposit, configure_logger):
    logger = configure_logger
    assert bank.close_deposit("002") == "Warning! Client not registered."
    logger.warning("Warning! A deposit is not opened. Reason: ClientId is not registered.")
