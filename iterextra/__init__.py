# -*- coding: utf-8 -*-


def chaincall(callables, *args, **kwargs):
    result = None
    for i, callable_ in enumerate(callables):
        if not i:
            result = callable_(*args, **kwargs)
        else:
            result = callable_(result)
    return result
