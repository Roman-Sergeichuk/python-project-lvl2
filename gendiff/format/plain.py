from gendiff import diff


def generate_plain_format(common_data, *, path=''):
    out_string = ''
    for key, (status, value) in sorted(common_data.items()):
        if status == diff.NESTED:
            out_string += generate_plain_format(value, path=(path + f'{key}.'))
        if status == diff.ADDED:
            if type(value) == dict:
                out_string += f"Property '{path}{key}' was added with value: 'complex value'\n"  # noqa: E501
            else:
                out_string += f"Property '{path}{key}' was added with value: '{value}'\n"  # noqa: E501
        if status == diff.REMOVED:
            out_string += f"Property '{path}{key}' was removed\n"
        if status == diff.CHANGED:
            val_before, val_after = value
            out_string += f"Property '{path}{key}' was changed. From " \
                          f"'{val_before}' to '{val_after}'\n"
    return out_string
