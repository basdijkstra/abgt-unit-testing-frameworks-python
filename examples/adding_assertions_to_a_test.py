import pytest


def test_add_2_and_2_should_equal_4():
    """ This test checks that 2 and 2 equals 4.
        As that is true, the test will pass
    """
    our_result = 2 + 2

    assert our_result == 4


def test_add_2_and_2_should_equal_5():
    """ This test checks that 2 and 2 equals 5.
        As that is true, the test will fail
    """
    our_result = 2 + 2

    assert our_result == 5


def test_add_2_and_2_should_equal_5_fails_with_supplied_message():
    """ This test, too, checks that 2 and 2 equals 5.
        As that is not true, the test will fail again,
        but this time with the specified message
    """
    our_result = 2 + 2

    assert our_result == 5, "2 and 2 should equal 5"


def test_create_boolean_with_value_true_check_that_value_is_true():
    """ This test uses an assertTrue to check that the value of
        a specified boolean variable is equal to 'True'.
    """
    our_boolean = True

    assert our_boolean is True


def test_create_variable_with_value_none_it_check_that_value_is_none():
    """ This test asserts that a variable has not been initialized
        (it has never been assigned a value, or it has explicitly
        been assigned the 'None' value).
    """
    our_variable = None

    assert our_variable is None


def test_check_dividing_by_zero_raises_zerodivisionerror():
    """ This test uses a 'with pytest.raises' construct
        to check that a code statement raises a specific type of error,
        in this case a ZeroDivisionError.
        As that is the case, the test will pass.
    """
    with pytest.raises(ZeroDivisionError):
        our_result = 2 / 0


def test_check_dividing_by_zero_raises_valueerror():
    """ This test uses a 'with pytest.raises' construct
        to check that a code statement raises a specific type of error,
        in this case a ValueError. As that is not the case,
        (it raises a ZeroDivisionError) the test will fail.
    """
    with pytest.raises(ValueError):
        our_result = 2 / 0


def test_check_dividing_by_zero_raises_zerodivisionerror_but_doesnt():
    """ This test uses a 'with pytest.raises' construct
        to check that a code statement raises a specific type of error,
        in this case a ZeroDivisionError.
        Since no error is raised at all, the test will fail.
    """
    with pytest.raises(ZeroDivisionError):
        our_result = 2 / 1
