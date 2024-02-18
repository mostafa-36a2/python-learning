"""
If a custom class doesn't have the __bool__ method, Python will look for the __len__() method.

If the __len__ is zero, the object is False. Otherwise, it's True.

If a class doesn't implement the __bool__ and __len__ methods, the objects of the class will evaluate to True.
"""
class A:
    items:list
    def __init__(self, member_int:int, member_str:str):
        """Constructor

        Args:
            member_int (int): first arg
            member_str (str): second arg
        >>> A(1,"test").items[0]
        1
        """
        self.items = list()
        self.items.append(member_int)
        self.items.append(member_str)

    def clear(self):
        self.items.clear()
        return self

    def __len__(self):
        """Testing __bool__
            >>> bool(A(1,"hi"))
            True
            >>> bool(A(0,"hi"))
            True
            >>> bool(A(1,""))
            True
            >>> bool(A(0,""))
            True
            >>> bool(A(123,"test").clear())
            False
        """
        return len(self.items)
