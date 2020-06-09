#!usr/bin/env python3
from gendiff.cli import get_parse_args
from gendiff.diff import generate_diff


def main():
    parser = get_parse_args()
    args = parser.parse_args()
    diff = generate_diff(
        args.first_file,
        args.second_file,
        out_format=args.format
    )
    print(diff)


if __name__ == '__main__':
    main()
