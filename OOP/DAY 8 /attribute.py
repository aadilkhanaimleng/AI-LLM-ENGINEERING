#Object ke andar jo information store hoti hai = Attribute

class Student:
    pass

student1 = Student()

student1.name = "Aadil"
student1.age = 19

print(student1.name)
print(student1.age) 

#student1 → Object
#name     → Attribute
#age      → Attribute
#Aadil    → name ki value
#19       → age ki value


#EXAMPLE 2
class Car:
    pass

car1 = Car()

car1.brand = "BMW"
car1.speed = 120

print(car1.brand)
print(car1.speed) 


#car1.brand → car1 ka brand attribute
#car1.speed → car1 ka speed attribute