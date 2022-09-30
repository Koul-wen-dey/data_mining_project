import readfile


class tree_node:
    def __init__(self, nam, num, par):
        self.name = nam
        self.number = num
        self.parents = par
        self.link = None
        self.children = {}
    
    def increase(self,num):
        self.number += num
    
class FP_tree():
    def __init__(self,file,min_sup):
        self.table = readfile.csv2table(file,min_sup)
        