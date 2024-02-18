"""x-__bool__.py script

>>> 1+1
2
"""
class A:
    """A class
    >>> True
    True
    """
    member_int:int
    member_str:str
    def __init__(self, member_int:int, member_str:str):
        """Constructor

        Args:
            member_int (int): first arg
            member_str (str): second arg
        >>> A(1,"test").member_int
        1
        """
        self.member_int = member_int
        self.member_str = member_str

    def __bool__(self):
        """Testing __bool__
            >>> bool(A(1,"hi"))
            True
            >>> bool(A(0,"hi"))
            True
            >>> bool(A(1,""))
            True
            >>> bool(A(0,""))
            False
        """
        return bool(self.member_int) or bool(self.member_str)
