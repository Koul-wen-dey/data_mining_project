from FP_Tree import FP_tree as fp
from collections import defaultdict as dicts
'''
a = {
    1: ['z', 'r'],
    2: ['z', 'x', 'y', 's', 't'],
    3: ['z'],
    4: ['x', 's', 'r'],
    5: ['z', 'x', 'y', 'r', 't'],
    6: ['z', 'x', 'y', 's', 't']
}

a = {
    1: ['bread', 'milk', 'beer'],
    2: ['bread', 'coffee'],
    3: ['bread', 'egg'],
    4: ['bread', 'milk', 'coffee'],
    5: ['milk', 'egg'],
    6: ['bread', 'egg'],
    7: ['milk', 'egg'],
    8: ['bread', 'milk', 'egg', 'beer'],
    9: ['bread', 'milk', 'egg']
}
'''
a = {
    1:['bread','milk','vegetable','fruit','eggs'],
    2:['noodle','beef','pork','water','socks','gloves','shoes','rice'],
    3:['socks','gloves'],
    4:['bread','milk','shoes','socks','eggs'],
    5:['socks','shoes','sweater','cap','milk','vegetable','gloves'],
    6:['eggs','bread','milk','crab','shrimp','rice']
}

c = dicts(lambda:0)
for i in a.keys():
    for j in a[i]:
        c[j] += 1

c = dict(filter(lambda a:a[1]>2,c.items()))
c = dict(sorted(c.items(),key=lambda i:i[1],reverse=True))
for k in a.keys():
    a[k] = list(filter(lambda s:s in c.keys(),a[k]))
for k in a.keys():
    a[k].sort(key=lambda x:(c[x],x),reverse=True)
print(a)
print(c)
b = fp()
b.table = a
b.header = c
b.build()
b.mining_pattern()
# print(b.pattern)
# b.show_result()
