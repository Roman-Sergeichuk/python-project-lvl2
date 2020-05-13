#!usr/bin/env python3
from gendiff.cli import get_parse_args, get_formatted_string
from gendiff.gendiff import generate_diff


def main():
    args = get_parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    get_formatted_string(diff)


if __name__ == '__main__':
    main()
