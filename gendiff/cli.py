import argparse


def get_parse_args():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f',
        '--format',
        type=str,
        default='nested',
        choices=['nested', 'plain', 'json'],
        help='set format of output'
    )
    return parser
