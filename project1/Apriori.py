import readfile
import csv
from itertools import combinations

class AP():
    def __init__(self,support=0.002,confidence=0.6):
        self.min_support = support
        self.min_confidence = confidence
        self.frequent_pattern = []
        self.header = {}

    def get_table(self,file:str):
        table1 = {1:[1, 3, 4], 2:[2, 3, 5], 3:[1, 2, 3, 5], 4:[2, 5]}
        self.total_num = 4
        header1 = {1:2,2:3,3:3,4:1,5:3}
        # table1, header1,self.total_num = readfile.csv2table(file)
        self.table = []
        for t in table1.items():
            self.table.append(frozenset(t[1]))
        for h in header1.items():
            self.header[frozenset({h[0]})] = h[1]/self.total_num


    def filter_candidate(self,Ck:list):
        freq = readfile.dicts(lambda:0)
        result = []
        for d in self.table:
            for candidate in Ck:
                if candidate.issubset(d):
                    freq[candidate] += 1
        for k in freq.keys():
            sup = freq[k]/self.total_num
            if sup >= self.min_support:
                result.append(k)
            self.header[k] = sup
        return result

    def apriori_generate(self,Lk:list,k:int):
        result = []
        for i in range(len(Lk)):
            for j in range(i+1,len(Lk)):
                l1 = list(Lk[i])[:k-2].sort()
                l2 = list(Lk[j])[:k-2].sort()
                if l1 == l2:
                    result.append(frozenset(Lk[i] | Lk[j]))
        return result

    def build(self):
        C1 = sorted([i for i in self.header.keys()])
        L1 = self.filter_candidate(C1)
        self.frequent_pattern.append(L1)
        k = 2
        while len(self.frequent_pattern[k-2]) > 0:
            Ck = self.apriori_generate(self.frequent_pattern[k-2],k)
            Lk = self.filter_candidate(Ck)
            if len(Lk) == 0:
                break
            self.frequent_pattern.append(Lk)
            k += 1
        pass
    
    def find_rule(self,fp:frozenset,current_fp:frozenset):

        pass

    def generate_rules(self):
        self.rules = set()
        for fp in self.frequent_pattern:
            if len(fp) > 1:
                self.find_rule(fp,fp)
        
        for r in self.rules:
            print(r)

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