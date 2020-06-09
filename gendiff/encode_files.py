import yaml
import json
import os


def get_data(file):
    _, file_extension = os.path.splitext(file)
    if file_extension.lower() == '.json':
        file_data = json.load(open(file))
    elif file_extension.lower() == '.yml' or file_extension.lower() == '.yaml':
        file_data = yaml.safe_load(open(file))
    else:
        raise ValueError(
            'Unsupported file format. Can use only .json and .yml/.yaml files'
        )
    return file_data
