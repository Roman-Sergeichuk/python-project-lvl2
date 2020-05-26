

def make_tags_and_common_data(dict_before, dict_after):
    tags = {}
    common_data = {}
    dict_before_keys = set(dict_before.keys())
    dict_after_keys = set(dict_after.keys())

    common_keys = list(dict_before_keys & dict_after_keys)
    deleted_keys = list(dict_before_keys - dict_after_keys)
    added_keys = list(dict_after_keys - dict_before_keys)

    common_keys.sort()
    deleted_keys.sort()
    added_keys.sort()

    for key in common_keys:
        value_before = dict_before[key]
        value_after = dict_after[key]

        if value_before == value_after:
            tags[key] = 'non_modified'
            common_data[key] = value_after
            continue

        value_before_is_dict = isinstance(value_before, dict)
        value_after_is_dict = isinstance(value_after, dict)
        if value_before_is_dict and value_after_is_dict:
            common_data[key], tags[key] = make_tags_and_common_data(value_before, value_after)  # noqa: E501
        else:
            tags[f'{key}_deleted'] = 'modified_deleted'
            tags[f'{key}_added'] = 'modified_added'
            common_data[f'{key}_deleted'] = value_before
            common_data[f'{key}_added'] = value_after

    for key in added_keys:
        value_after = dict_after[key]
        tags[key] = 'added'
        common_data[key] = value_after

    for key in deleted_keys:
        value_before = dict_before[key]
        tags[key] = 'deleted'
        common_data[key] = value_before
    return common_data, tags
