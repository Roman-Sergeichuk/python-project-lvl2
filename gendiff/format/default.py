import json
from gendiff.format.string_editor import add_prefix, remove_postfix


def generate_nested_format(common_data, tags):
    out_string = json.dumps(common_data, indent=4, separators=('', ': ')).replace('"', '')  # noqa: E501
    out_string = add_prefix(out_string, tags)
    out_string = remove_postfix(out_string, postfix='_deleted')
    out_string = remove_postfix(out_string, postfix='_added')
    return out_string
