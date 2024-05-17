#!/usr/bin/env python3
"""Encrypting passwords with bcrypt and
checking them with bcrypt module"""

import re
from typing import List
import logging


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    """retrns the log message obfuscated by redacting
    the fields specified in fields using redaction"""
    for field in fields:
        return (re.sub(r'{}=.*?{}'.format(field, separator),
                         '{}={}{}'.format(field, redaction,
                                          separator), message))

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
