import yaml
import json
import os
import sys


def make_dict_if_file_is_none(data):
    return {} if data is None else data


def get_data(file):
    file_name, file_extension = os.path.splitext(file)
    if file_extension == '.json':
        file_data = json.load(open(file))
    elif file_extension == '.yml' or file_extension == '.yaml':
        file_data = yaml.safe_load(open(file))
    else:
        sys.exit('Unsupported file format. Can use only .json and .yml/.yaml files')  # noqa: E501
    data = make_dict_if_file_is_none(file_data)
    return data
