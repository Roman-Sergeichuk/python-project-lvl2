import argparse


def get_parse_args():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', default='nested', help='set format of output')  # noqa: E501
    args = parser.parse_args()
    return args
