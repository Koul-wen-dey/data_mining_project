import readfile
from itertools import combinations

class AP():
    def __init__(self,support=0.002,confidence=0.6):
        self.min_support = support
        self.min_confidence = confidence

    def get_table(self,file:str):
        table1, header1,self.total_num = readfile.csv2table(file)
        self.header = dict(filter(lambda a:a[1]/self.total_num>=self.min_support,header1.items()))
        
        for k in table1.keys():
            table1[k] = list(filter(lambda s:s in self.header.keys(),table1[k]))
        self.table = dict(filter(lambda v:v[1],table1.items()))

        # print(self.table)
    def build(self):
        k = 2
        while True:
            tmpset = set()
            for item in self.table.items():
                cb = combinations(item[1],k)
                for c in cb:
                    tmpset.add(c)
            break
        # for t in tmpset:
            # print(t)