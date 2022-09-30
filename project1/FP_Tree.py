import readfile


class tree_node:
    def __init__(self, i, c, p):
        self.item = i
        self.count = c
        self.parent = p
        self.link = None
        self.children = {}
    
    def increase(self,num):
        self.number += num
    
class FP_tree():
    def __init__(self):
        self.header = {}
        self.root = tree_node(0,1,None)

    def update_tree(self,item):
        # node = tree_node(item,1,None)
        if item in self.

        pass
    def update_header(self):
        pass




    def build(self,file,min_sup):
        self.table, self.header = readfile.csv2table(file,min_sup)
        for transaction in self.table.items():
            for item in transaction:
                self.update_tree(i[1])
