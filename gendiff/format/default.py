from gendiff import diff


def format_complex_value(complex_value, prefix, indent):
    result = '{'
    tab = '    '
    for key, value in complex_value.items():
        if isinstance(value, dict):
            result += f'\n{indent}{prefix}{key}: ' \
                      f'{format_complex_value(value, prefix, indent=indent + tab)}'  # noqa: E501
        else:
            result += f'\n{indent}{prefix}{key}: {value}'
    indent = indent[:-len(prefix)]
    result += '\n'
    result += indent + '}'
    return result


def generate_nested_format(common_data, *, indent='    '):
    out_string = '{'
    prefix_add = '+ '
    prefix_remove = '- '
    prefix_non_changed = '  '
    tab = '    '
    for key, (status, value) in sorted(common_data.items()):
        if status == diff.NESTED:
            out_string += f'\n{indent}{key}: ' \
                          f'{generate_nested_format(value, indent=indent + tab)}'  # noqa: E501
        elif status == diff.EQUAL:
            out_string += f'\n{indent}{prefix_non_changed}{key}: {value}'
        elif status == diff.CHANGED:
            val_before, val_after = value
            out_string += f'\n{indent}{prefix_add}{key}: {val_after}'
            out_string += f'\n{indent}{prefix_remove}{key}: {val_before}'
        elif status == diff.ADDED:
            if isinstance(value, dict):
                out_string += f'\n{indent}{prefix_add}{key}: ' \
                              f'{format_complex_value(value, prefix=prefix_non_changed, indent=indent + tab)}'  # noqa: E501
            else:
                out_string += f'\n{indent}{prefix_add}{key}: {value}'
        elif status == diff.REMOVED:
            if isinstance(value, dict):
                out_string += f'\n{indent}{prefix_remove}{key}: ' \
                              f'{format_complex_value(value, prefix=prefix_non_changed, indent=indent + tab)}'  # noqa: E501
            else:
                out_string += f'\n{indent}{prefix_remove}{key}: {value}'
    indent = indent[:-len(tab)]
    if out_string != '{':
        out_string += '\n'
    out_string += indent + '}'
    return out_string
