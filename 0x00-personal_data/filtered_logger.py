#!/usr/bin/env python3
"""
This module contains functions and classes for filtering and formatting logs
with sensitive data redacted.
"""

import re
import logging
from typing import List


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    """
    Returns the log message with sensitive fields obfuscated.

    Args:
        fields (List[str]): List of fields to obfuscate.
        redaction (str): The string to replace sensitive field values with.
        message (str): The log line containing sensitive data.
        separator (str): The character separating fields in the log line.

    Returns:
        str: The obfuscated log message.
    """
    pattern = r'({}=)[^{}]+'.format("|".join(fields), separator)
    return re.sub(pattern, r'\1' + redaction, message)


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class for formatting log records with sensitive
    information redacted.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the formatter with fields to redact.

        Args:
            fields (List[str]): List of field names to redact in log messages.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record, obfuscating sensitive fields.

        Args:
            record (logging.LogRecord): The log record to format.

        Returns:
            str: The formatted log record with sensitive data redacted.
        """
        record.msg = filter_datum(
                self.fields,
                self.REDACTION,
                record.getMessage(), self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)
