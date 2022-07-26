Python 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import simplest
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import simplest
ModuleNotFoundError: No module named 'simplest'
>>> import simpleset
>>> simpleset
<module 'simpleset' from 'C:\\Python39\\lib\\simpleset.py'>
>>> a=[1,2,3]
>>> b=[3,4,5]
>>> simpleset.union(a,b)
[1, 2, 3, 4, 5]
>>> simpleset.intersect(a,b)
[3]
>>> dir(simpleset)
['WRAPPER_ASSIGNMENTS', 'WRAPPER_UPDATES', '__builtins__', '__cached__', '__doc__', '__file__', '__intersectSC', '__loader__', '__name__', '__package__', '__spec__', 'cache', 'cached_property', 'cmp_to_key', 'difference', 'intersect', 'lru_cache', 'partial', 'partialmethod', 'reduce', 'singledispatch', 'singledispatchmethod', 'total_ordering', 'union', 'update_wrapper', 'wraps']
>>> 