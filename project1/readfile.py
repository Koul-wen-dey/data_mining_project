import csv
from collections import defaultdict as dicts


'''
minimum support seems to be less than 1%, otherwise there will left a null set.
'''

file_path = './inputs/project1_testing_dataset.csv'
min_sup = 0.003

def csv2table(file,min_sup):
    with open(file,newline='') as csvfile:
        lists = [list(map(int,row)) for row in csv.reader(csvfile,delimiter=',')]
    table = dicts(list)
    sup = dicts(lambda:0)
    total_num = len(lists)

    for l in lists:
        table[l[0]].append(l[-1])
        sup[l[-1]] += 1
    sup = dict(filter(lambda a:a[1]/total_num>=min_sup,sup.items()))
    sup = dict(sorted(sup.items(),key=lambda i:-i[1]))
    print(sup)

    for k in table.keys():
        table[k] = list(filter(lambda s:s in sup.keys(),table[k]))
    table1 = dict(filter(lambda v:v[1],table.items()))

    for k in table.keys():
        table[k].sort(key=lambda x:sup[x])
        table[k].reverse()
    # print(table1.items())
    return table1,sup

csv2table(file_path,min_sup)