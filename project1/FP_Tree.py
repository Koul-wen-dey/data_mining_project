from tkinter.messagebox import NO
import readfile


class tree_node:
    def __init__(self, i, c, p):
        self.item = i
        self.count = c
        self.parent = p
        self.link = None
        self.children = {}

    def increase(self):
        self.count += 1


class FP_tree():
    def __init__(self):
        self.header = {}
        self.root = tree_node(0, 1, None)

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
        # print(self.header)

    def get_table(self, file: str, min_sup: float):
        self.table, self.header = readfile.csv2table(file, min_sup)

    def mining_pattern(self):
        if len(self.header) == 0:
            return
        self.pattern = []
        for value in self.header.items():
            node_now = value[1][1]

            while node_now is not None:
                node_tmp = node_now
                tmp = []
                while node_tmp is not self.root:
                    tmp.append(node_tmp.item)
                    node_tmp = node_tmp.parent
                self.pattern.append(tmp)
                node_now = node_now.link

    def inorder_print(self, tmp: tree_node):
        print(tmp.item, tmp.count)
        for t in tmp.children.values():
            self.inorder_print(t)

    def show_result(self):
        self.inorder_print(self.root)
