#!/usr/bin/env python3

from datetime import date


class Person(object):
    """
    This is the super class
    """

    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name


class Instructor(Person):
    """
    Inherits from Person class
    """

    def __init__(self, f_name, l_name, courses):
        super().__init__(f_name, l_name)
        self.courses = courses


class Student(Person):
    """
    Inherits from person
    """
    # student class variable
    current_id = 0

    def __init__(self, f_name, l_name, courses):
        super().__init__(f_name, l_name)
        self.courses = courses
        self.id = self.generate_id()

    def attend_class(self, date, **kwargs):
        """
        Attend class function
        """
        if date == date.today():
            Db.attendance_list[self.id] = [self.f_name, self.l_name]

    def generate_id(self):
        """
        Increment class variable with new method call for each instance
        Assing it to instance
        """
        Student.current_id += 1
        i_d = Student.current_id
        return i_d


class Db():
    """
    storage class
    """
    attendance_list = {}
