#!/usr/bin/env python
""" function called filter_datum that returns
the log message obfuscated"""

import re


def filter_datum(fields:list, redaction:str,
                message:str, obfuscated:str) -> str:
    """
    Returns the log message obfuscated.
    """
    regex = '|'.join(map(re.escape, fields))
    return re.sub(regex, redaction, message)
