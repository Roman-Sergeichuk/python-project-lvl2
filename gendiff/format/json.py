import json
from gendiff.format.string_editor import remove_postfix


def make_data_for_json(common_data, tags):
    new_data = {}
    changed_values = {}
    for key, value in common_data.items():
        tag = tags[key]
        if type(value) == dict and type(tag) == dict:
            new_data[key] = make_data_for_json(value, tag)
        elif tag == 'modified_added' or tag == 'modified_deleted':
            changed_values[tag] = value
            if 'modified_added' in changed_values and 'modified_deleted' in changed_values:  # noqa: E501
                old_value = changed_values['modified_deleted']
                new_value = changed_values['modified_added']
                new_data[key] = ('changed', (old_value, new_value))
                changed_values = {}
        else:
            new_data[key] = (tag, value)
    return new_data


def generate_json_format(common_data, tags):
    common_data_with_tags = make_data_for_json(common_data, tags)
    out_string = json.dumps(common_data_with_tags, indent=4)
    out_string = remove_postfix(out_string, postfix='_deleted')
    out_string = remove_postfix(out_string, postfix='_added')
    return out_string
