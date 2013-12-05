# -*- coding: utf-8 -*-
from functools import partial

__all__ = ["chaincall", "pick"]


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

def pick(member):
    """Picks ``member`` from object.

    It is intended to be used with ``map``

    >>> lst = [complex(1.0, 2.0), complex(1.5, 2.5)]
    >>> list(map(pick('imag'), lst))
    [2.0, 2.5]
    """

    def picker(obj):
        return getattr(obj, member)
    picker.__doc__ = "Picks member '{0}' from ``obj``".format(member)
    picker.__name__ = "{0}_picker".format(member)
    return picker
