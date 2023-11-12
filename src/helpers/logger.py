import logging
from settings import logging_settings

JSON_FORMATTER = logging.Formatter(
    '{"time": "%(asctime)s", "level": "%(levelname)s", "logger": "%(name)s", "message": "%(message)s"}'
)

LOG_LEVELS = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
}


def get_logger(logger_name: str) -> logging.Logger:
    log_level = LOG_LEVELS.get(logging_settings.log_level, logging.INFO)
    log_to_file = logging_settings.log_to_file
    log_to_console = logging_settings.log_to_console
    log_file_path = logging_settings.log_file_path

    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)

    # Clear existing handlers to avoid duplication when reconfiguring
    for existing_handler in logger.handlers:
        logger.removeHandler(existing_handler)

    if logger.getEffectiveLevel() <= logging.DEBUG:
        # In debug mode, use a non-JSON formatter for better readability
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
    else:
        formatter = JSON_FORMATTER  # JSON formatter

    if log_to_console:
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    if log_to_file:
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
