from FP_Tree import FP_tree
import Apriori as ap


'''
    minimum support seems to be less than 1%, otherwise there will left a null set.
'''
file_path = './inputs/ibm_2022_release.csv'
min_sup = 7
min_con = 0.6

if '__main__' == __name__:
    ft = FP_tree(support=min_sup,confidence=min_con)
    ft.get_table(file_path)
    ft.build()
    ft.mining_pattern()
    print(ft.table)
    # print(ft.header)
    # ft.build()
    # ft.show_result()
