from gendiff.encode_files import get_data
from gendiff.format.default import generate_nested_format
from gendiff.format.plain import generate_plain_format
from gendiff.format.json import generate_json_format


EQUAL, CHANGED, ADDED, REMOVED, NESTED = 'equal', 'changed', 'added', 'removed', 'nested'  # noqa: E501


def make_common_data(before_data, after_data):
    common_data = {}

    common_keys = before_data.keys() & after_data.keys()
    added_keys = after_data.keys() - before_data.keys()
    removed_keys = before_data.keys() - after_data.keys()

    for key in common_keys:
        if type(before_data[key]) == dict and type(after_data[key]) == dict:
            common_data[key] = (NESTED, make_common_data(before_data[key], after_data[key]))  # noqa: E501
        elif before_data[key] == after_data[key]:
            common_data[key] = (EQUAL, after_data[key])
        else:
            common_data[key] = (CHANGED, (before_data[key], after_data[key]))
    for key in added_keys:
        common_data[key] = (ADDED, after_data[key])
    for key in removed_keys:
        common_data[key] = (REMOVED, before_data[key])
    return common_data


def make_formatted_string(common_data, *, format):
    if format == 'nested':
        out_string = generate_nested_format(common_data)
    if format == 'plain':
        out_string = generate_plain_format(common_data)
    if format == 'json':
        out_string = generate_json_format(common_data)
    return out_string


def generate_diff(first_file, second_file, *, out_format):
    before_data = get_data(first_file)
    after_data = get_data(second_file)
    common_data = make_common_data(before_data, after_data)
    out_string = make_formatted_string(common_data, format=out_format)
    return out_string
