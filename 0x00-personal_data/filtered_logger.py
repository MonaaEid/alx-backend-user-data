#!/usr/bin/env python
"""function called filter_datum that returns
the log message obfuscated"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                    message: str, separator: str) -> str:
        """returns the log message obfuscated"""
        for field in fields:
            message = re.sub(r'{}=.*?{}'.format(field, separator), '{}={}{}'
                          .format(field, redaction, separator), message)
        return message