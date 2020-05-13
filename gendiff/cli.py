import argparse
import json


def get_parse_args():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    return args


def get_formatted_string(data):
    print(json.dumps(data, indent=2, separators=('', ': ')).replace('"', ''))  # noqa: E501
