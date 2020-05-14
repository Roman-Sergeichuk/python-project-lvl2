from gendiff.encoder import get_data
import json


def generate_diff(first_file, second_file):
    first_file_data = get_data(first_file)
    second_file_data = get_data(second_file)
    diff_data = {}
    for key, value in second_file_data.items():
        if key in first_file_data and value == first_file_data[key]:
            diff_data[f'  {key}'] = value
        elif key in first_file_data and value != first_file_data[key]:
            diff_data[f'+ {key}'] = value
            diff_data[f'- {key}'] = first_file_data[key]
        else:
            diff_data[f'+ {key}'] = value
    for key, value in first_file_data.items():
        if key not in second_file_data:
            diff_data[f'- {key}'] = value
    diff_string = json.dumps(diff_data, indent=2, separators=('', ': ')).replace('"', '')  # noqa: E501
    return diff_string
