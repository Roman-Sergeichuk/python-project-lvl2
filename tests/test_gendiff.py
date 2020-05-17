from gendiff.gendiff import generate_diff


def test_compare_non_empty_plain_files():
    with open('./tests/fixtures/expected_plain_common_diff.txt', 'r') as fixture:
        expected = fixture.read()
    assert expected == generate_diff(
        './tests/fixtures/before.json',
        './tests/fixtures/after.json'
    )
    assert expected == generate_diff(
        './tests/fixtures/before.yml',
        './tests/fixtures/after.yml'
    )


def test_compare_empty_files():
    assert generate_diff(
        './tests/fixtures/empty.json',
        './tests/fixtures/empty.json'
    ) == '{}'
    assert generate_diff(
        './tests/fixtures/empty.yml',
        './tests/fixtures/empty.yml'
    ) == '{}'


def test_complex_files():
    with open('./tests/fixtures/expected_nested_common_diff.txt', 'r') as fixture:
        expected = fixture.read()
    assert expected == generate_diff(
        './tests/fixtures/before_nested.json',
        './tests/fixtures/after_nested.json'
    )
    assert expected == generate_diff(
        './tests/fixtures/before_nested.yml',
        './tests/fixtures/after_nested.yml'
    )
