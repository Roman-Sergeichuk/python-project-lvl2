from gendiff.format.default import generate_nested_format
from gendiff.format.plain import generate_plain_format


def make_formatted_string(common_data, tags, *, format):
    if format == 'nested':
        out_string = generate_nested_format(common_data, tags)
    if format == 'plain':
        out_string = generate_plain_format(common_data, tags)
    return out_string
