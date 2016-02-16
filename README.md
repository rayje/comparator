comparator
====

A python library to compare objects

Install
-------
Using `pip install`
```
pip install git+git://github.com/rayje/comparator.git
```

Using `pip install -r requirements.txt`
- Add the following to your `requirements.txt` file:
```
-e git+git://github.com/rayje/comparator.git#egg=comparator
```

Usage
-----
```python
from comparator import Dict

first = {'a':1, 'b': 2}
second = {'b':2, 'a':1}

d1 = Dict(first)
d2 = Dict(second)

print d1 == d2   # True

m1 = {'test':34, 'unknown':55, 'xyz':0}
m2 = {'test':34, 'unknown':55, 'abc':0, 'idx': 0}

dm1 = Dict(m1, ['xyz'])
dm2 = Dict(m2, non_matching_keys=['abc', 'idx'])

print dm1 == dm2  # True
print dm1 != d2   # True
print dm2 == d1   # False
```

License
=======
The MIT License (MIT)

Copyright (c) 2016 Rayland Jeans

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
