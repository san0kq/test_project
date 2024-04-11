import logging
import os

def get_logger(name: str) -> logging.Logger:
    """Get a logger with the specified name.

    Args:
        name (str): The name of the logger.

    Returns:
        logging.Logger: The logger object.
    """

    loglevel = os.environ.get('LOGLEVEL', 'DEBUG').upper()
    logging.basicConfig(level=loglevel, format='[%(asctime)s]|<%(levelname)-7s>|: [%(name)s.py].[%(funcName)s:%(lineno)d]:> %(message)s',
                        datefmt="[%Y/%m/%d %H:%M;%S]",
                        handlers=[logging.StreamHandler()])
    return logging.getLogger(name)
