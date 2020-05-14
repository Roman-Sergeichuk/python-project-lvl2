import yaml
import json
import os


def make_dict_if_file_is_none(data):
    return {} if data is None else data


def get_data(file):
    file_name, file_extension = os.path.splitext(file)
    if file_extension == '.json':
        file_data = json.load(open(file))
    elif file_extension == '.yml' or file_extension == '.yaml':
        file_data = yaml.safe_load(open(file))
    data = make_dict_if_file_is_none(file_data)
    return data
