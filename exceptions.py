class Error(Exception):
    """
    Base Class for other Exception
    """
class UnsuccessfulRequest(Error):
    """
    Raised when status_code != 200
    """
class ArgOutOfRange(Error):
    """
    Raised when passed argument is out of range
    """
