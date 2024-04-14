#!/usr/bin/python3
"""Module for say_my_name method."""

def say_my_name(first_name, last_name=""):
    """Method for printing first and last name.

    Args:
        first_name: first name string.
        last_name: last name string.

    Raises:
        TypeError: If first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Check if last_name is an empty string or consists only of whitespace
    if last_name.strip() == "":
        print("My name is {:s}".format(first_name))
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
