from gendiff.encoder import get_data
from gendiff.format.make_formatted_string import make_formatted_string
from gendiff.tags_and_common_data import make_tags_and_common_data


def generate_diff(first_file, second_file, *, out_format):
    before_data = get_data(first_file)
    after_data = get_data(second_file)
    common_data, tags = make_tags_and_common_data(before_data, after_data)
    out_string = make_formatted_string(common_data, tags, format=out_format)
    return out_string
