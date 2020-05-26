def remove_postfix(string, *, postfix):
    return string.replace(postfix, '')


def make_key_prefix(data_string, key, *, prefix):
    prefix_length = len(prefix)
    indent_to_delete = ' ' * prefix_length
    old_key = f'{indent_to_delete}{key}'
    new_key = f'{prefix}{key}'
    return data_string.replace(old_key, new_key)


def add_prefix(data_string, tags):
    out_string = data_string
    for key, tag in tags.items():
        if type(tag) == dict:
            out_string = add_prefix(out_string, tag)
        else:
            if 'deleted' in tag:
                out_string = make_key_prefix(out_string, key, prefix='- ')
            elif 'added' in tag:
                out_string = make_key_prefix(out_string, key, prefix='+ ')
    return out_string
