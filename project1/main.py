from FP_Tree import FP_tree
import Apriori as ap


'''
    minimum support seems to be less than 1%, otherwise there will left a null set.
'''
file_path = './inputs/project1_testing_dataset.csv'
min_sup = 0.005
min_con = 0

if '__main__' == __name__:
    ft = FP_tree()
    ft.get_table(file_path, min_sup)
    ft.build()
    # ft.show_result()
