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
        tmptable = [i for i in self.table.values()]
        while True:
            tmpset = set()
            tmpfrq = readfile.dicts(lambda:0)
            for item in tmptable:
                cb = combinations(item,k)
                for c in cb:
                    # tmpset.add(c)
                    tmpfrq[c]+=1
            rmfrq = dict(filter(lambda x:x[1]/self.total_num<self.min_support,tmpfrq.items()))
            tmpfrq = dict(filter(lambda x:x[1]/self.total_num>=self.min_support,tmpfrq.items()))
            # for tmp

            break
        for t in rmfrq.items():
            print(t)