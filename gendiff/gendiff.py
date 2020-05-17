from gendiff.encoder import get_data
import json


def get_common_keys(dict1, dict2):
    keys_of_dict1 = set(dict1.keys())
    keys_of_dict2 = set(dict2.keys())
    intersection = keys_of_dict1.intersection(keys_of_dict2)
    common_keys = list(intersection)
    return sorted(common_keys)


def get_added_keys(dict1, dict2):
    keys_of_dict1 = set(dict1.keys())
    keys_of_dict2 = set(dict2.keys())
    difference = keys_of_dict2.difference(keys_of_dict1)
    added_keys = list(difference)
    return sorted(added_keys)


def get_deleted_keys(dict1, dict2):
    keys_of_dict1 = set(dict1.keys())
    keys_of_dict2 = set(dict2.keys())
    difference = keys_of_dict1.difference(keys_of_dict2)
    deleted_keys = list(difference)
    return sorted(deleted_keys)


def get_render(dictionary):
    result_string = json.dumps(dictionary, indent=2, separators=('', ': ')).replace('"', '')  # noqa: E501
    return result_string


def keys_update(before_data, after_data):
    added_keys = get_added_keys(before_data, after_data)
    deleted_keys = get_deleted_keys(before_data, after_data)
    common_keys = get_common_keys(before_data, after_data)
    common_data = {}
    for key in common_keys:
        before_value = before_data[key]
        after_value = after_data[key]
        if before_value == after_value:
            common_data[f'  {key}'] = after_value
        else:
            if type(before_value) != dict and type(after_value) != dict:
                common_data[f'+ {key}'] = after_value
                common_data[f'- {key}'] = before_value
            else:
                common_data[key] = keys_update(before_value, after_value)
    for key in added_keys:
        common_data[f'+ {key}'] = after_data[key]
    for key in deleted_keys:
        common_data[f'- {key}'] = before_data[key]
    return common_data


def generate_diff(first_file, second_file):
    before_data = get_data(first_file)
    after_data = get_data(second_file)
    common_data = keys_update(before_data, after_data)
    result = get_render(common_data)
    return result
