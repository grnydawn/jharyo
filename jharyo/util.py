# -*- coding: utf-8 -*-
"""Jharyo utility module."""

from __future__ import absolute_import, division, print_function

class NameSpace(object):
    pass

def error_exit(msg):
    print("Error: %s"%msg)
    sys.exit(-1)


def extract_opt(argv, opts, nargs):

    if len(argv) < 2:
        return [], argv

    extracts = [];
    newargv = []
    skip = -1

    for idx, arg in enumerate(argv):

        if skip >= 0:
            extracts[-1].append(arg)
            skip -= 1
            continue

        if arg in opts:
            skip = nargs
            extracts.append([])
        else:
            newargv.append(arg)

    import pdb; pdb.set_trace()
    return extracts, newargv
