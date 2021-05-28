def test_this_method_is_identified_as_a_test():
    """ Because the name of this method starts with 'test',
        pytest identifies it as a test method.
    """
    pass


def test_this_method_is_also_identified_as_a_test():
    """ This method, too, is identified as a test method by pytest,
        since its name starts with 'test'
    """
    pass


def this_method_is_not_identified_as_a_test():
    """ Because the name of this method does not start with 'test',
        pytest doesn't see it as a test method.
    """
    pass
