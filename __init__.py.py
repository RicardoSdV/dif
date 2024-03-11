"""Paste dicts here to find their diff"""

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'a': 1, 'b': 4, 'd': 5}


print 'Items Diff'
common_keys = set(d1.keys()) & set(d2.keys())
for key in common_keys:
    if d1[key] != d2[key]:
        print '(d1 & d2).key:', key
        print 'd1.value', d1[key]
        print 'd2.value', d2[key], '\n'


print 'D1 Exclusive Keys'
d1_exclusive_keys = set(d1.keys()) - set(d2.keys())
for key in d1_exclusive_keys:
    print 'd1.key:', key
    print 'd1.value:', d1[key], '\n'

print 'D2 Exclusive Keys'
d2_exclusive_keys = set(d2.keys()) - set(d1.keys())
for key in d2_exclusive_keys:
    print 'd2.key:', key
    print 'd2.value:', d2[key], '\n'

# TODO: Make this capable of traversing any data structure of any depth and make prints of great beauty
# TODO: Including traversing strings, for example, to print the diff of two call stacks
