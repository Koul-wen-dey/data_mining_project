from FP_Tree import FP_tree
from Apriori import AP
import args


# file_path = './inputs/ibm_2022_release.csv'
# min_sup = 5
# min_con = 0.6

if '__main__' == __name__:
    a = args.parse_args()
    file_path = 'inputs/'+ a.dataset
    # ft = FP_tree(support=a.min_sup,confidence=a.min_conf)
    # ft.get_table(file_path)
    # ft.build()
    # ft.mining_pattern()
    # ft.generate_rules()
    # ft.writecsv()

    ap = AP(support=a.min_sup,confidence=a.min_conf)
    ap.get_table(file_path)
    ap.build()