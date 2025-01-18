import logging


def setup_logger(name: str = "app") -> logging.Logger:
    """
    Sets up a centralized logger for the application.

    This function creates and configures a logger with a console handler
    that outputs log messages to the standard output (typically the console).
    It also sets the default log level to INFO and formats the log messages.

    Args:
        name (str): The name of the logger. Default is "app".

    Returns:
        logging.Logger: The configured logger instance.

    Example:
        logger = setup_logger("myapp")
        logger.info("This is an info message")
    """
    # Create the logger instance
    default_logger = logging.getLogger(name)

    # Set the default logging level
    default_logger.setLevel(logging.INFO)

    # Create a console handler for outputting logs to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Create a formatter for log message structure
    formatter = logging.Formatter("%(levelname)s - %(message)s")
    console_handler.setFormatter(formatter)

    # Attach the console handler to the logger
    default_logger.addHandler(console_handler)

    return default_logger


logger = setup_logger()
