import json


def generate_diff(first_file, second_file):
    first = json.load(open(first_file))
    second = json.load(open(second_file))
    new_dict = {}
    for key, value in second.items():
        if key in first and value == first[key]:
            new_dict[f'  {key}'] = value
        elif key in first and value != first[key]:
            new_dict[f'+ {key}'] = value
            new_dict[f'- {key}'] = first[key]
        else:
            new_dict[f'+ {key}'] = value
    for key, value in first.items():
        if key not in second:
            new_dict[f'- {key}'] = value
    diff = json.dumps(new_dict, indent=2, separators=('', ': ')).replace('"', '')  # noqa: E501
    return diff
