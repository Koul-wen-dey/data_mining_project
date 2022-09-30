from FP_Tree import FP_tree as fp

a = {
    1:['z','r'],
    2:['z','x','y','s','t'],
    3:['z'],
    4:['x','s','r'],
    5:['z','x','y','r','t'],
    6:['z','x','y','s','t']
}
b = fp()
for trans in a.items():
    b.update_tree(trans[1])
b.show_result(b.root)