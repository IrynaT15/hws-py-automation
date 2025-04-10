import pytest
import logging


def pytest_addoption(parser):
    parser.addoption(
        "--log_level",
        action="store",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
    )


@pytest.fixture(scope="session")
def configure_logger(request):
    log_level = request.config.getoption("--log_level")
    logger = logging.getLogger()
    logger.setLevel(log_level)
    formatter = logging.Formatter(
        "%(asctime)s : %(levelname)s : %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger
