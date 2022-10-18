import argparse

def parse_args():
    p = argparse.ArgumentParser()

    def a(*args, **kwargs):
        p.add_argument(*args, **kwargs)

    a('--min_sup', type=float, default=0.3, help='Minimum support')
    a('--min_conf', type=float, default=0.6, help='Minimum confidence')
    a('--dataset', type=str, default='2022-DM-release-testdata-2.csv', help='Dataset to use, please include the extension')

    return p.parse_args()