import readfile


class tree_node:
    def __init__(self, i, c, p):
        self.item = i
        self.count = c
        self.parent = p
        self.link = None
        self.children = {}
    
    def increase(self, n):
        self.count += n
    
class FP_tree():
    def __init__(self):
        self.header = {}
        self.root = tree_node(0,1,None)

    def update_tree(self,item):
        # node = tree_node(item,1,None)
        tmp = self.root
        for i in item:
            if i in tmp.children.keys():
                tmp.children[i].count += 1
            else:
                tmp.children[i] = tree_node(i,1,tmp)
            
            tmp = tmp.children[i]

    def update_header(self):
        pass

    def show_result(self,tmp:tree_node):
        print(tmp.item,tmp.count)
        for t in tmp.children.values():
            self.show_result(t)
        

    def build(self,file,min_sup):
        self.table, self.header = readfile.csv2table(file,min_sup)
        for transaction in self.table.items():
            for item in transaction:
                self.update_tree(item[1])
