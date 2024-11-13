#!/usr/bin/env python3
""" Main 0
"""
from api.v1.auth.auth import Auth

a = Auth()

# Test the methods
print(a.require_auth("/api/v1/status/", ["/api/v1/status/"]))  # Expected: False
print(a.authorization_header())  # Expected: None
print(a.current_user())  # Expected: None
