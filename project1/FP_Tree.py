import readfile
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
    def __init__(self):
        self.header = {}
        self.root = tree_node(0, 1, None)
        self.threshold = 2

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

    def update_cond(self, item:list):
        tmp = self.root
        for i in item:
            if i in tmp.children.keys():
                tmp.children[i].increase()
            else:
                tmp.children[i] = tree_node(i,1,tmp)
            tmp = tmp.children[i]


    def build(self):
        for h in self.header.keys():
            self.header[h] = [self.header[h], None]
        for transaction in self.table.items():
            self.update_tree(transaction[1])
        # print(self.header)

    def get_table(self, file: str, min_sup: float):
        self.sup = min_sup
        self.table, self.header = readfile.csv2table(file, min_sup)

    def find_fp(self,prefix):

        pass

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
        self.frequent_pattern = set()
        
        for value in reversed(self.header.items()):
            patterns = readfile.dicts(lambda:0)
            node_now = value[1][1]
            prefixs = self.find_prefix(node_now)

            for p in prefixs:
                for i in p:
                    patterns[i] += 1
            patterns = dict(filter(lambda v:v[1]>=self.threshold,patterns.items()))
            prefixs = list(patterns.keys())

            for i in range(1,len(prefixs)+1):
                cb = combinations(prefixs,i)
                for j in cb:
                    self.frequent_pattern.add(j)
        for fp in self.frequent_pattern:
            print(fp)

            

    def inorder_print(self, tmp: tree_node):
        print(tmp.item, tmp.count)
        for t in tmp.children.values():
            self.inorder_print(t)

    def show_result(self):
        self.inorder_print(self.root)
