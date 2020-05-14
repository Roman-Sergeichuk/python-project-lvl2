#!usr/bin/env python3
from gendiff.cli import get_parse_args
from gendiff.gendiff import generate_diff


def main():
    args = get_parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
