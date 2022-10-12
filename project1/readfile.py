import csv
from collections import defaultdict as dicts



# file_path = './inputs/project1_testing_dataset.csv'
# min_sup = 0.005

def csv2table(file):
    # open file and initialize dict
    with open(file,newline='') as csvfile:
        lists = [list(map(str,row)) for row in csv.reader(csvfile,delimiter=',')]
    table = dicts(list)
    sup = dicts(lambda:0)
    # total_num = len(lists)

    # make transection and count elements number
    for l in lists:
        table[int(l[0])].append(int(l[-1]))
        sup[int(l[-1])] += 1
    '''
    # filter with minimum support and sort supports
    sup = dict(filter(lambda a:a[1]/total_num>=min_sup,sup.items()))
    sup = dict(sorted(sup.items(),key=lambda i:i[1],reverse=True))

    # filter table with supports and filter null list transection
    for k in table.keys():
        table[k] = list(filter(lambda s:s in sup.keys(),table[k]))
    table1 = dict(filter(lambda v:v[1],table.items()))

    # sort elements in transection with support
    for k in table1.keys():
        table1[k].sort(key=lambda x:(sup[x],x),reverse=True)
    print(table1.items())
    '''
    return table, sup, len(table)

# csv2table(file_path,min_sup)