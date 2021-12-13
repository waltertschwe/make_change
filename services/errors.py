class Error(Exception):
    """
    Base class for other exceptions
    """

    pass


class ValueTooSmallError(Error):
    """
    Raised when the input value is too small
    """

    pass


class NoChangeRequired(Error):
    """
    Raised when the input value matches the amount owed.
    """

    pass
