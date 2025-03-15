# Настройте ротацию файлов логов,
# чтобы каждый день создавался новый файл с датой в имени файла.
# Ограничьте количество хранимых файлов логов до 7, чтобы старые файлы автоматически удалялись.

import logging
from logging.handlers import TimedRotatingFileHandler


def setup_log_day_timed_rotation():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "%(asctime)s : %(levelname)s : %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    handler = TimedRotatingFileHandler(
        "file.log",
        when ="d",
        interval=1,
        backupCount=7,
        encoding="utf-8"
    )
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)

    logger.addHandler(handler)


setup_log_day_timed_rotation()
