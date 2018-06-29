# -*- coding: utf-8 -*-
"""Jharyo Main module."""

import sys

from .error import InternalError, UsageError
from .util import NameSpace, error_exit
from .parse import ArgParser
from .load import load_data
from .transform import transform_data
from .present import present_data

# TODO: support deamon mode

def entry():
    return main(sys.argv[1:])

def main(argv):

    try:

        ns = NameSpace()
        args = ArgParser(argv)

        if args.command in ("plot", "show"):

            # load data
            for data in load_data(ns, args):

                # transform data
                new_data = transform_data(data, ns, args)

                # present data
                present_data(new_data, ns, args)
        else:
            pass

    except InternalError as err:

        error_exit(str(err))

    except UsageError as err:

        error_exit(str(err))

    else:
        return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

