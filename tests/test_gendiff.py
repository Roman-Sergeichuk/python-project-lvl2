from gendiff.gendiff import generate_diff


with open('./tests/fixtures/expected1_json.txt', 'r') as fixture:
    expected1 = fixture.read()

with open('./tests/fixtures/expected2_json.txt', 'r') as fixture:
    expected2 = fixture.read()

with open('./tests/fixtures/expected3_json.txt', 'r') as fixture:
    expected3 = fixture.read()


def test_gendiff():
    assert expected1.replace('\n', '') == generate_diff(
        './tests/fixtures/before_full.json',
        './tests/fixtures/after_modified.json'
    ).replace('\n', '')

    assert expected2.replace('\n', '') == generate_diff(
        './tests/fixtures/before_empty.json',
        './tests/fixtures/after_modified.json'
    ).replace('\n', '')

    assert expected3.replace('\n', '') == generate_diff(
        './tests/fixtures/before_full.json',
        './tests/fixtures/after_empty.json'
    ).replace('\n', '')


