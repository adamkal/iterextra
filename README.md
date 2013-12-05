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

pick - helper function to make fetching member of list of objects a little more
       clear

```
import iterextra

lst = [complex(1.0, 2.0), complex(1.5, 2.5)]

assert map(pick('imag'), lst) == [1.5, 2.5]
```
