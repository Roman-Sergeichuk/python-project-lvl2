from gendiff.gendiff import generate_diff


def test_compare_non_empty_flat_files():
    with open('./tests/fixtures/expected_flat_common_diff.txt', 'r') as fixture:
        expected = fixture.read()
    assert expected == generate_diff(
        './tests/fixtures/before.json',
        './tests/fixtures/after.json',
        out_format='nested'
    )
    assert expected == generate_diff(
        './tests/fixtures/before.yml',
        './tests/fixtures/after.yml',
        out_format='nested'
    )


def test_compare_empty_files():
    assert generate_diff(
        './tests/fixtures/empty.json',
        './tests/fixtures/empty.json',
        out_format='nested'
    ) == '{}'
    assert generate_diff(
        './tests/fixtures/empty.yml',
        './tests/fixtures/empty.yml',
        out_format='nested'
    ) == '{}'
    assert generate_diff(
        './tests/fixtures/empty.json',
        './tests/fixtures/empty.json',
        out_format='plain'
    ) == ''
    assert generate_diff(
        './tests/fixtures/empty.yml',
        './tests/fixtures/empty.yml',
        out_format='plain'
    ) == ''


def test_complex_files():
    with open('./tests/fixtures/expected_nested_common_diff.txt', 'r') as fixture:
        expected = fixture.read()
    assert expected == generate_diff(
        './tests/fixtures/before_nested.json',
        './tests/fixtures/after_nested.json',
        out_format='nested'
    )
    assert expected == generate_diff(
        './tests/fixtures/before_nested.yml',
        './tests/fixtures/after_nested.yml',
        out_format='nested'
    )


def test_plain_format():
    with open('./tests/fixtures/plain_expected_common_diff.txt', 'r') as fixture:
        expected = fixture.read()

    assert expected == generate_diff(
        './tests/fixtures/before_nested.json',
        './tests/fixtures/after_nested.json',
        out_format='plain'
    )
    assert expected == generate_diff(
        './tests/fixtures/before_nested.yml',
        './tests/fixtures/after_nested.yml',
        out_format='plain'
    )


def test_json_format():
    with open('./tests/fixtures/json_expected_common_diff.txt', 'r') as fixture:
        expected = fixture.read()

    assert expected == generate_diff(
        './tests/fixtures/before_nested.json',
        './tests/fixtures/after_nested.json',
        out_format='json'
    )
    assert expected == generate_diff(
        './tests/fixtures/before_nested.yml',
        './tests/fixtures/after_nested.yml',
        out_format='json'
    )
