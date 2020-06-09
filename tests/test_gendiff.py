from gendiff.diff import generate_diff
import os
import json


def get_fixture(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    fixture = os.path.join(current_dir, 'fixtures', file_name)
    return fixture


check = {
    'flat_expected.txt': (
        'before.json',
        'before.yml',
        'after.json',
        'after.yml',
        'nested'
    ),
    'nested_expected.txt': (
        'before_nested.json',
        'before_nested.yml',
        'after_nested.json',
        'after_nested.yml',
        'nested'
    ),
    'plain_expected.txt': (
        'before_nested.json',
        'before_nested.yml',
        'after_nested.json',
        'after_nested.yml',
        'plain'
    ),
    'empty_expected_nested.txt': (
        'empty.json',
        'empty.yml', 'empty.json',
        'empty.yml',
        'nested'
    ),
    'empty_expected_plain.txt': (
        'empty.json',
        'empty.yml',
        'empty.json',
        'empty.yml',
        'plain'
    )
         }


def test_text_format():
    for expected_data, init_data in check.items():
        before_json, before_yaml, after_json, after_yaml, check_format = init_data  # noqa:E501

        with open(get_fixture(expected_data), 'r') as fixture:
            expected = fixture.read()

        assert expected == generate_diff(
            get_fixture(before_json),
            get_fixture(after_json),
            out_format=check_format
        )
        assert expected == generate_diff(
            get_fixture(before_json),
            get_fixture(after_yaml),
            out_format=check_format
        )
        assert expected == generate_diff(
            get_fixture(before_yaml),
            get_fixture(after_yaml),
            out_format=check_format
        )


def test_json_format():
    fixture = get_fixture('json_expected.json')
    expected = json.load(open(fixture))
    print(expected)

    check_json = generate_diff(
        get_fixture('before_nested.json'),
        get_fixture('after_nested.json'),
        out_format='json'
    )
    check_yaml = generate_diff(
        get_fixture('before_nested.yml'),
        get_fixture('after_nested.yml'),
        out_format='json'
    )
    assert expected == json.loads(check_json)
    assert expected == json.loads(check_yaml)

