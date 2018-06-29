# -*- coding: utf-8 -*-
"""Jharyo Main module."""

import sys

from .error import InternalError, UsageError
from .util import NameSpace, error_exit
from .parse import ArgParser
from .load import load_data
from .transform import transform_data
from .present import present_data

def _main(chunk, msgs):

    try:
        args = msgs['args']
        ns = NameSpace()
        ns.update(msgs['funcs'])

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

        error_exit(err.num, err.attrs)

    except UsageError as err:

        error_exit(err.num, err.attrs)

    else:
        return 0

def entry():
    return main(sys.argv[1:])

# NOTE: no join but sync

def _handle_import_function_opt(argv):

    funcs = {}

    opts, newargv = extract_opt(argv, ('--import-function',), 1)

    for opt in opts:
        namemap, target, kwargs = parse_subargs(namemap=True, sep=':', nargs=1)
        content = load_target(target)
        g = {}
        l = {}
        exec(content, g, l)
        for new, old in namemap.items():
            funcs[new] = g[old]

    return funcs, newargv

def _handle_parallel_opt(argv, funcs):

    chunks = None

    # extract parallel opt
    opts, newargv = extract_opt(argv, ('--parallel',), 1)

    # eval if required
    if len(opts) > 0:
        # use only the last one
        vargs, kwargs = funcargs_eval(opts[-1])
        if len(vargs) == 1: # the first arg is chunk definition
            if vargs[0] in funcs:
                chunks = safe_eval('%s(%s)'%(vargs[0], funcs[vargs[0]]))
            else:
                chunks = safe_eval(vargs[0])
        else:
            error_exit(1, {'vargs': vargs}) 

    return chunks, opts, newargv

def main(argv):

    try:

        chunks = []
        funcs = {}

        import pdb; pdb.set_trace()
        args = ArgParser(argv)

        if args.import_function:
            funcs, argv = _handle_import_function_opt(argv)

        if args.parallel:
            chunks, parallel_opts, argv = _handle_parallel_opt(argv, funcs)

        # check if parallel
        if chunks:
            manager = Manager()
            msgs = manager.dict()
            msgs['args'] = args
            msgs['funcs'] = funcs
            msgs['parallel'] = parallel_opts

            for chunk in chunks:
                proc = Process(target=_main, args=(chunk, msgs))
                proc.start()
                proc.join()
        else:
            msgs = {}
            msgs['args'] = args
            msgs['funcs'] = funcs
            msgs['parallel'] = None
                       
            return _main(chunks, msgs)

    except InternalError as err:

        error_exit(err.num, err.attrs)

    except UsageError as err:

        error_exit(err.num, err.attrs)

    else:
        return 0




if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

