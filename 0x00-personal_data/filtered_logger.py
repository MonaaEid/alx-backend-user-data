#!/usr/bin/env python
"""function called filter_datum that returns
the log message obfuscated"""

import re
from typing import List
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self):
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        NotImplementedError


def filter_datum(fields: List[str], redaction: str,message: str, separator: str) -> str:
        """returns the log message obfuscated"""
        for field in fields:
            message = re.sub(r'{}=.*?{}'.format(field, separator), '{}={}{}'.format(field, redaction, separator), message)
        return message
