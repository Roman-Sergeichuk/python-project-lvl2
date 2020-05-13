import yaml
import json
import os


def get_data(file):
    file_name, file_extension = os.path.splitext(file)
    if file_extension == '.json':
        file_data = json.load(open(file))
    elif file_extension == '.yml' or file_extension == '.yaml':
        file_data = yaml.safe_load(open(file))
    return file_data
