from gendiff.gendiff import generate_diff





def test_compare_non_empty_files():
    with open('./fixtures/expected_common_diff.txt', 'r') as fixture:
        expected = fixture.read()
    assert expected == generate_diff(
        './fixtures/before.json',
        './fixtures/after.json'
    )


def test_compare_empty_files():
    with open('./fixtures/expected_empty.txt', 'r') as fixture:
        expected = fixture.read()
    assert expected == generate_diff(
        './fixtures/empty.json',
        './fixtures/empty.json'
    )