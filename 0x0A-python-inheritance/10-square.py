#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    methods:
    __init__(self, size)
    """
    def __init__(self, size):
        """
        Args:
            size(int): private
        """
        self.integer_validator('size", size)
        super().__init__(size, size)
        self.size = size
