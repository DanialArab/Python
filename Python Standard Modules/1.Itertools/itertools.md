These are good pointes to remember:
- I can do groupby (from itertools import groupby)
- I can find word pairs using pairwise (from itertools import pairwise). pairwise returns consecutive pairs of elements from an iterable.
- I can get all combinations of parameters using itertools.product
- itertools.compress(data, selectors) filters data, returning only those items where the corresponding value in selectors is truthy (non-zero).
- zip() is a built-in Python function that combines multiple iterables (like lists, tuples, etc.) element-wise into tuples. zip() returns an iterator in Python 3 — which means you need to convert it to a list or loop over it to see the values.

