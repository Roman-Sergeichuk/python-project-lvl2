from gendiff.format.string_editor import remove_postfix


def is_dict(value):
    return type(value) == dict


def make_line_added(path, key, value):
    if is_dict(value):
        value = 'complex value'
    return f"\nProperty '{path}{key}' was added with value: '{value}'"


def make_line_deleted(path, key):
    return f"\nProperty '{path}{key}' was removed"


def make_line_modified(path, key, old_value, new_value):
    return f'\nProperty \'{path}{key}\' was changed. From \'{old_value}\' to \'{new_value}\''  # noqa: E501


def generate_plain_format(common_data, tags):
    init_out_string = ''
    init_path = ''

    def inner(inner_common_data, inner_tags, out_string, property_path):
        changed_values = {}
        for key, value in inner_common_data.items():
            tag = inner_tags[key]
            if is_dict(tag):
                out_string = inner(value, tag, out_string, property_path=(property_path + f'{key}.'))  # noqa: E501
            if tag == 'added':
                out_string = out_string + make_line_added(property_path, key, value)  # noqa: E501
            if tag == 'deleted':
                out_string = out_string + make_line_deleted(property_path, key)
            if tag == 'modified_deleted' or tag == 'modified_added':
                changed_values[tag] = value
                print(changed_values)
                if 'modified_deleted' in changed_values and 'modified_added' in changed_values:  # noqa: E501
                    key = remove_postfix(key, postfix='_deleted')
                    key = remove_postfix(key, postfix='_added')
                    old_value = changed_values['modified_deleted']
                    new_value = changed_values['modified_added']
                    out_string = out_string + make_line_modified(property_path, key, old_value, new_value)  # noqa: E501
                    changed_values = {}
        return out_string
    return inner(common_data, tags, init_path, init_out_string)
