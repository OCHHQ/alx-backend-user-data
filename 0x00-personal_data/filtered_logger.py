#!/usr/bin/env python3
import re


def filter_datum(fields, redaction, message, separator):
    """
    Obfuscates the values for the given fields in the log message
    Args:
        fields (list): A list of strings representing the fields to obfuscate.
        redaction (str): A string representing the obfuscation marker.
        message (str): A string representing the log line.
        separator (str): A string representing the character
        separating all fields in the log line.
    Returns:
        str: The log message with the specified fields obfuscated.
    """
    pattern = r"({})=(.+?)({}|$)".format("|".join(fields), separator)
    return re.sub(pattern, r"\1=\2" + redaction + r"\3", message)
