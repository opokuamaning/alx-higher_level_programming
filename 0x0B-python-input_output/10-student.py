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

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance

        Return:
             only attribute names contained in this list
        """

        if attrs is None:
            return self.__dict__
        else:
            dic = {}
            for att in attrs:
                if att in self.__dict__.keys():
                    dic[att] = self.__dict__[att]
            return dic
