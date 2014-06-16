[![Build Status](https://travis-ci.org/adamkal/iterextra.png)](https://travis-ci.org/adamkal/iterextra)
[ ![Codeship Status for adamkal/iterextra](https://www.codeship.io/projects/8875e420-d76e-0131-ba27-52e8c0de9e09/status)](https://www.codeship.io/projects/23879)
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

```python
import iterextra

lst = [complex(1.0, 2.0), complex(1.5, 2.5)]

assert map(pick('imag'), lst) == [1.5, 2.5]
```
