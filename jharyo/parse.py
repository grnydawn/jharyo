# -*- coding: utf-8 -*-
"""Jharyo argument parser module."""

from __future__ import absolute_import, division, print_function

from .util import extract_opt

class ArgParser(object):

    def __init__(self, argv):

        self._template, newargv = self._handle_template(argv)
        self._actions, self._args = self._parse_arguments(newargv)

    def _handle_template(self, argv):

        opts, newargv = extract_opt(argv, ('-i', '--import'), 1)

        if len(opts) > 1:
            error_exit('More than one templates are imported.')
        elif len(opts) == 1:
            return self._load_template(opts[0]), newargv
        else:
            return None, newargv
