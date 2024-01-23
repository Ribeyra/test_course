from test_course.capitalize import capitalize


def test_capitalize():
    assert capitalize('hello') == 'Hello'
    assert capitalize('1ello') == '1ello'
    print('\ntest_capitalize - pass')


def test_capitalize_for_int():
    assert capitalize(12) == 12
    print('\ntest_capitalize_for_int - pass')


def test_capitalize_for_empty_str():
    assert capitalize('') == ''
    print('\ntest_capitalize_for_empty_str - pass')
