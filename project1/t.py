from FP_Tree import FP_tree as fp
'''
a = {
    1: ['z', 'r'],
    2: ['z', 'x', 'y', 's', 't'],
    3: ['z'],
    4: ['x', 's', 'r'],
    5: ['z', 'x', 'y', 'r', 't'],
    6: ['z', 'x', 'y', 's', 't']
}
'''
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
    1:['br','mi','ve','fr','eg'],
    2:['no','be','po','wa','so','gl','sh','ri'],
    3:['so','gl'],
    4:['br','mi','sh','so','eg'],
    5:['so','sh','sw','ca','mi','ve','gl'],
    6:['eg','br','mi','cr','sh','ri']
}
'''
c = {
    'bread': 7,
    'milk': 6,
    'egg': 6,
    'coffee': 2,
    'beer': 2
}
b = fp()
b.table = a
b.header = c
b.build()
b.mining_pattern()
# print(b.pattern)
# b.show_result()
