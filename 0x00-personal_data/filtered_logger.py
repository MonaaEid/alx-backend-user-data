#!/usr/bin/env python
""" function called filter_datum that returns
the log message obfuscated"""


def filter_datum(
        fields: list,
        redaction: str,
        message: str,
        separator: str) -> str:
    """
    returns the log message obfuscated
    """
    for field in fields:
        message = message.replace(field + separator, redaction + separator)
    return message
