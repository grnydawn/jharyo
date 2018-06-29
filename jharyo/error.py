# -*- coding: utf-8 -*-
"""Jharyo error handling module."""

from __future__ import absolute_import, division, print_function

class Error(Exception):
    pass

class InternalError(Error):
    pass

class UsageError(Error):
    pass

