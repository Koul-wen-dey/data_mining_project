import readfile
import csv
from itertools import combinations

class AP():
    def __init__(self,support=0.002,confidence=0.6):
        self.min_support = support
        self.min_confidence = confidence
        self.frequent_pattern = []

    def get_table(self,file:str):
        table1, self.header,self.total_num = readfile.csv2table(file)
        # self.header = dict(filter(lambda a:a[1]/self.total_num>=self.min_support,header1.items()))
        self.table = []
        for t in table1.items():
            self.table.append(sorted(t[1]))
        # print(self.table)

    def filter_candidate(self,Ck:list,data:list):
        freq = readfile.dicts(lambda:0)
        Ck = map(frozenset,Ck)
        result = []
        for d in data:
            for candidate in Ck:
                if candidate.issubet(d):
                    freq[candidate] += 1
        for k in freq.keys():
            sup = freq[k]/self.total_num
            if sup >= self.min_support:
                result.append(k)
        # self.header.update()
        return result

    def apriori_generate(self,Lk,k):
        result = []
        for i in range(len(Lk)):
            for j in range(i+1,len(Lk)):
                l1 = list(Lk[i])[:k-2].sort()
                l2 = list(Lk[j])[:k-2].sort()
                if l1 == l2:
                    result.append(Lk[i] | Lk[j])
        return result

    def build(self):
        C1 = sorted([[i] for i in self.header.keys()])
        L1 = self.filter_candidate(C1,)
        k = 2
        while len(self.frequent_pattern[k-2]) > 0:
            Ck = self.apriori_generate(self.frequent_pattern[k-2],k)
            Lk = self.scan_data()
            # self.header.update(sup)
            if len(Lk) == 0:
                break
            self.frequent_pattern.append(Lk)
            k += 1
        pass

    # def build(self):
    #     k = 2
    #     tmptable = [i for i in self.table.values()]
    #     while True:
    #         tmpset = set()
    #         tmpfrq = readfile.dicts(lambda:0)
    #         for item in tmptable:
    #             cb = combinations(item,k)
    #             for c in cb:
    #                 # tmpset.add(c)
    #                 tmpfrq[c]+=1
    #         rmfrq = dict(filter(lambda x:x[1]/self.total_num<self.min_support,tmpfrq.items()))
    #         tmpfrq = dict(filter(lambda x:x[1]/self.total_num>=self.min_support,tmpfrq.items()))
    #         # for tmp

    #         break
    #     for t in rmfrq.items():
    #         print(t)

    def writecsv(self,filename:str):
        filename = 'outputs/' + filename.split('.')[0] + '-aprior.csv'
        with open(filename,'w',newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['antecedent','consequent','support','confidence','lift'])
            for r in self.rules:
                tmp = ''
                for i in r[0]:
                    tmp = tmp + str(i) + ' '
                tmp = '{' + tmp[:-1] + '}'
                tmp2 = ''
                for i in r[1]:
                    tmp2 = tmp2 + str(i) + ' '
                tmp2 = '{' + tmp2[:-1] + '}'
                writer.writerow([tmp, tmp2,r[2],r[3],r[4]])
            csvfile.close()