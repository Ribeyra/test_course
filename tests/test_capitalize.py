from test_course.capitalize import capitalize

if capitalize('hello') != 'Hello':
    raise Exception('fail1')
if capitalize('1ello') != '1ello':
    raise Exception('fail2')
if capitalize(12) != 12:
    raise Exception('fail3')
if capitalize('') != '':
    raise Exception('fail4')

print('pass')
