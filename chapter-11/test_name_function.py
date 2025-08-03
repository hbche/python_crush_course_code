from name_function import get_formatted_name

def test_first_last_name():
    """能够正确地处理像 Janis Joplin 这样的姓名吗？"""

    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'

def test_first_middle_last_name():
    """能够正确地处理像 Wolfgang Amadeus Mozart 这样的姓名吗？"""

    formatted_name = get_formatted_name('Wolfgang', middle_name='Amadeus', last_name='Mozart')
    assert formatted_name == 'Wolfgang Amadeus Mozart'

