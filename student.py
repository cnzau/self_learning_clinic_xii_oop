#!/usr/bin/env python3

from datetime import date

class Student(object):
    # student class variable
    current_id = 0
    
    def __init__(self, f_name, l_name):
        super(Student, self).__init__()
        self.id = self.generate_id()
        self.f_name = f_name
        self.l_name = l_name
    # Make at least 5 students attend class
    def attend_class(self, date, **kwargs):
        # Default output data if dict is not specified
        default_data = {teacher: 'Frank', location : 'Nairobi'}

        if kwargs is not None:
            if date == date.today():
                new_dict = {}
                # Student instance attended class in specified date (currently today)
                return True
            return False
        return default_data
    
    def generate_id(self):
        """
        Increment class variable with new method call for each instance
        Assing it to instance
        """
        Student.current_id += 1
        i_d = Student.current_id
        return i_d

