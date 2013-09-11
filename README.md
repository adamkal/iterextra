iterextra
=========

An extension to Python standard library itertools

Usage
-----

chaincall - chains function calls so that result of previous function is passed as argument to next one. 

```python

import iterextra

to_bool = iterextra.chaincall(int, bool)

assert to_bool("1")
assert not to_bool("0")

```
