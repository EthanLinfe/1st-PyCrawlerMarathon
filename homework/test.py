a = {}

if 1 not in a:
    a.update({1: {}})

a[1].update({1:1})
a[1].update({2:2})
print(a[1])