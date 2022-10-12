from FP_Tree import FP_tree as fp
from collections import defaultdict as dicts
from Apriori import AP
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
a1={}

c = dicts(lambda:0)
for i in a.keys():
    for j in a[i]:
        c[j] += 1

c1 = dict(filter(lambda a:a[1]>2,c.items()))
c1 = dict(sorted(c1.items(),key=lambda i:i[1],reverse=True))

for k in a.keys():
    a1[k] = list(filter(lambda s:s in c1.keys(),a[k]))
a = a1.copy()
for k in a1.keys():
    a1[k].sort(key=lambda x:(c1[x],x),reverse=True)
'''
b = fp(support=0.5)
b.table = a1
b.header = c1
b.total_num = 6
b.build()
b.mining_pattern()
b.generate_rules()
print()
'''
ap = AP(support=0.5)
ap.table = a
ap.header = c
for t in ap.table.items():
    print(t)
ap.build()