#self current object ko represent karta hai.


class Student:

    def __init__(self, name):
        self.name = name


student1 = Student("Aadil")

print(student1.name)