"""
Minimal shim of the stdlib `cgi` module for environments where it's removed
(e.g. Python 3.14). This provides the small surface area Cheetah expects at
import time (not a full replacement).
"""
from html import escape as _html_escape


class FieldStorage:
    def __init__(self, *args, **kwargs):
        # Minimal placeholder; real parsing isn't required for tests.
        self.value = None


def escape(s, quote=False):
    return _html_escape(s, quote=quote)


# Provide deprecated alias used by some packages
escape.__name__ = 'escape'
