#!/usr/bin/python3
"""
A class Student
Instantiates first_name, last_name and age
and has public method def to_json(self):
that retrieves a dictionary representation of a Student instance
"""


class Student():
    """
    Public attributes:
        first_name
        last_name
        age
    Public Methods:
        to_json
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialises student with full name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        retrieves a dictionary representation of a Student instance
        """

        return self.__dict__
