#Mandy and Viviana
#C: The__str__() Function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + "("+ str(self.age) + ")"

p1 = Person("John", 36)

print(p1)

#We believe that it would print out both the name and his age on the same line.
#In the first one, we printed them separately, but in this one we have them on the same line.
#Although, it just be in age in () after the name.

