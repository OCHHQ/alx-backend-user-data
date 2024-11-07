#!/usr/bin/env python3
"""Module for filtering sensitive information in log messages."""

import re


def filter_datum(fields, redaction, message, separator):
    """Obfuscates specified fields in the log message."""
    pattern = f"({'|'.join(fields)})=([^\\{separator}]*)"
    return re.sub(pattern, f"\\1={redaction}", message)
