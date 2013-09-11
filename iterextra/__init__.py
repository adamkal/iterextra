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
    """Chains function calls so that result of previous function is passed as
    argument to next one.

    >>> to_bool = chaincall(int, bool)
    >>> to_bool("1")
    True
    >>> to_bool("0")
    False
    """

    return partial(_chain_calls, args)
