"""
TEST CLEANER
IN PROGRESS
"""

from webapp.modules.tools.clean_sentence import remove_special_char


def test_if_remove_special_char_return_expected_data():

    mock = remove_special_char("a[b\"c/\\d:e?f!g-h}i>j<k(l)m{n,o]p&", "all")
    assert mock == "abcdefghijklmnop"

    # ADD SPACE FOR ==> " or - or ,
    mock = remove_special_char("I\"m testing-remove special char,thanks",
                               "add_space")
    assert mock == "i m testing remove special char thanks"
