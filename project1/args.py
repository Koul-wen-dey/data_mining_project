import argparse

def parse_args():
    p = argparse.ArgumentParser()

    def a(*args, **kwargs):
        p.add_argument(*args, **kwargs)

    a('--min_sup', type=float, default=0.002, help='Minimum support')
    a('--min_conf', type=float, default=0.002, help='Minimum confidence')
    a('--dataset', type=str, default='ibm-2022-release.csv', help='Dataset to use, please include the extension')

    return p.parse_args()