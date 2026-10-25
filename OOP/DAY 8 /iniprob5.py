class student:

    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course

student1=student("aadil",19,"AI")     
student2=student("rahul",10,"ML")

print(student1.name, student1.age, student1.course)
print(student2.name, student2.age, student2.course)
