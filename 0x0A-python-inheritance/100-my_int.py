#!/usr/bin/python3


class MyInt(int):
    """
    From original int
    """

    def __eq__(self, other):
        return (int(self) != other)

    def __ne__(self, other):
        return (int(self) == other)
