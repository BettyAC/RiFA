import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--prefix', required=True, help='Prefix to be added to the folder name')
args = parser.parse_args()
