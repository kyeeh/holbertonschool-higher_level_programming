#!/usr/bin/python3


class Student:
    """
    Student class.
    """

    def __init__(self, first_name, last_name, age):
        """
        Constructor method
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        dictionary representation of a Student instance with attrs validation
        """
        if (attrs and len(attrs) > 0):
            new_dict = {}
            my_dictv = vars(self)
            set_dict = set(my_dictv)
            set_list = set(attrs)
            keys = list(set_dict & set_list)
            for key in keys:
                new_dict[key] = my_dictv[key]
            return (new_dict)
        return vars(self)
