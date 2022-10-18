import readfile
import csv
from itertools import combinations


class tree_node:
    def __init__(self, i, c, p):
        self.item = i
        self.count = c
        self.parent = p
        self.link = None
        self.children = {}

    def increase(self, c = 1):
        self.count += c


class FP_tree():
    def __init__(self,support=0.002,confidence=0.6):
        self.header = {}
        self.root = tree_node(0, 1, None)
        self.min_support = support
        self.min_confidence = confidence

    def update_header(self, head: tree_node, tail: tree_node):
        while head.link is not None:
            head = head.link
        head.link = tail

    def update_tree(self, item: list):
        tmp = self.root
        for i in item:
            if i in tmp.children.keys():
                tmp.children[i].increase()
            else:
                tmp.children[i] = tree_node(i, 1, tmp)
                if self.header[i][1] is None:
                    self.header[i][1] = tmp.children[i]
                else:
                    self.update_header(self.header[i][1], tmp.children[i])
            tmp = tmp.children[i]

    def build(self):
        for h in self.header.keys():
            self.header[h] = [self.header[h], None]
        for transaction in self.table.items():
            self.update_tree(transaction[1])
        # for h in self.header.items():
            # print(h)
        
    def get_table(self, file: str):
        table1, header1,self.total_num = readfile.csv2table(file)
        # print(self.total_num)
        # filter with minimum support and sort supports
        header1 = dict(filter(lambda a:a[1]/self.total_num>=self.min_support,header1.items()))
        self.header = dict(sorted(header1.items(),key=lambda i:i[1],reverse=True))

        # filter table with supports and filter null list transection
        for k in table1.keys():
            table1[k] = list(filter(lambda s:s in self.header.keys(),table1[k]))
        self.table = dict(filter(lambda v:v[1],table1.items()))

        # sort elements in transection with support
        for k in self.table.keys():
            self.table[k].sort(key=lambda x:(self.header[x],x),reverse=True)

        # for h in self.header.items():
            # print(h)
        
    def find_prefix(self,node:tree_node):
        patterns=[]
        while node is not None:
            node_tmp = node
            tmp = []
            tmp.append(node_tmp.count)
            while node_tmp is not self.root:
                tmp.append(node_tmp.item)
                node_tmp = node_tmp.parent
            tmp.reverse()
            for i in range(tmp[-1]):
                patterns.append(tmp[:-1])
            node = node.link
        
        return patterns

    def mining_pattern(self):
        if len(self.header) == 0:
            return
        self.frequent_pattern = []
        tmp = set()
        self.frequency = readfile.dicts(lambda:0)
        for h in self.header.items():
            self.frequency[frozenset({h[0]})] = h[1][0]
        for value in reversed(self.header.items()):
            patterns = readfile.dicts(lambda:0)
            node_now = value[1][1]
            prefixs = self.find_prefix(node_now)

            for p in prefixs:
                for i in p:
                    patterns[i] += 1
            patterns = dict(filter(lambda v:v[1]/self.total_num>=self.min_support,patterns.items()))
            prefixs = list(patterns.keys())
            num = patterns[prefixs[0]]

            for i in range(1,len(prefixs)+1):
                cb = combinations(prefixs,i)
                for j in cb:
                    tmp.add(frozenset(j))
                    self.frequency[frozenset(j)] = num if num > self.frequency[frozenset(j)] else self.frequency[frozenset(j)]
                   
        for fp in tmp:
            self.frequent_pattern.append(fp)
        
        # for f in self.frequent_pattern:
            # print(f)

    def mining_pattern2(self):
        if len(self.header) == 0:
            return
        self.frequent_pattern = []
        tmp = set()
        self.frequency = readfile.dicts(lambda:0)

        for value in reversed(self.header.items()):
            patterns = readfile.dicts(lambda:0)
            node_now = value[1][1]
            prefixs = self.find_prefix(node_now)

    def find_rule(self,fp:frozenset,current_fp:frozenset):

        def remove_target(item,current_fp:frozenset):
            tmp = list()
            for cfp in current_fp:
                if cfp != item:
                    tmp.append(cfp)
            return frozenset(tmp)
        
        powerset = set()
        for i in range(1,len(fp)+1):
            cb = list(combinations(fp,i))
            for j in cb:
                powerset.add(frozenset(j))
        
        for p in powerset:
            others = fp - p
            for i in range(1,len(others)+1):
                cb = list(combinations(others,i))
                for j in cb:
                    confidence = round(self.frequency[frozenset.union(p,frozenset(j))] / self.frequency[p],3)
                    
                    if confidence >= self.min_confidence:
                        support = round(self.frequency[frozenset.union(p,frozenset(j))] / self.total_num,3)
                        lift = round(confidence / (self.frequency[frozenset(j)]/self.total_num),3)
                        self.rules.add((p,frozenset(j),support,confidence,lift))

    def generate_rules(self):
        self.rules = set()
        for fp in self.frequent_pattern:
            if len(fp) > 1:
                self.find_rule(fp,fp)
        
        for r in self.rules:
            print(r)

    
    def writecsv(self,filename:str):
        filename = 'outputs/' + filename.split('.')[0] + '-fp_growth.csv'
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


    def inorder_print(self, tmp: tree_node):
        print(tmp.item, tmp.count)
        for t in tmp.children.values():
            self.inorder_print(t)

    def show_result(self):
        self.inorder_print(self.root)
