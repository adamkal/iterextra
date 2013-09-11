# -*- coding: utf-8 -*-
from functools import partial


def _chain_calls(callables, *args, **kwargs):
    result = None
    for i, callable_ in enumerate(callables):
        if not i:
            result = callable_(*args, **kwargs)
        else:
            result = callable_(result)
    return result


def chaincall(*args):
    return partial(_chain_calls, args)
