#!/usr/bin/env python3
from datetime import date
from student import Student, Instructor, Db

# Create instructor
frank = Instructor('Tamre', 'Frank', ['Angular', 'Android'])

# Creat students
alex = Student('Alex', 'K.', ['Python', 'Angular'])
austin = Student('Austin', 'K.', ['Ruby'])
ancent = Student('Ancent', 'M.', ['React'])
vigie = Student('Vigie', 'M.', ['Android'])
lenny = Student('Lenny', 'R.', ['PHP', 'Angular'])
chris = Student('Chris', 'N.', ['Python', 'React'])
mueni = Student('Mueni', 'N.', ['Ruby'])
marius = Student('Marius', 'F.', ['PHP', 'Angular'])
steve = Student('Steve', 'K.', ['Python', 'Angular'])
clem = Student('Clement', 'N.', ['Node', 'Angular'])

# Make at least 5 students attend class
austin.attend_class(date=date.today(), bag='black', laptop='macbook')
steve.attend_class(bag='black', laptop='lenovo', date=date.today())
vigie.attend_class(bag='black', laptop='asus', date=date.today())
clem.attend_class(bag='black', laptop='acer', date=date.today())
mueni.attend_class(bag='black', laptop='macbook', date=date.today())


d = Db.attendance_list
print(sorted(d.items()))

