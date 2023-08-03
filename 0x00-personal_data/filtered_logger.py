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
