#!/usr/bin/env python3
"""Module for filtering log messages"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Obfuscates specified fields in a log message

    Args:
        fields (List[str]): List of fields to obfuscate
        redaction (str): String to replace field values with
        message (str): Log message
        separator (str): Field separator

    Returns:
        str: Obfuscated log message
    """
    for field in fields:
        message = re.sub(f'{field}=[^{separator}]*',
                         f'{field}={redaction}', message)
    return message

class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initializes RedactingFormatter with given fields

        Args:
            fields (List[str]): List of fields to obfuscate
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Filters values in incoming log records

        Args:
            record (logging.LogRecord): Log record

        Returns:
            str: Formatted log record
        """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super().format(record)

