# -*- coding: utf-8 -*-
"""Jharyo argument parser module."""

from __future__ import absolute_import, division, print_function

class ArgParser(object):

    def __init__(self, argv):

        self._template, newargv = self._handle_template(argv)
        self._actions, self._args = self._parse_arguments(newargv)
