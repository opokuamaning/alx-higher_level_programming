#!/usr/bin/python3
"""
Module: Rectangle class
Inherits base class
"""
from models.base import Base



class Rectangle(Base):
    """
    Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

