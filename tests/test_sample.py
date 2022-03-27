"""
Sample App Tests
"""

from sample.biz import my_func


def test_my_func():
    """my_func returns expected result"""
    result = my_func("one", "two")
    assert result == "one:two"
