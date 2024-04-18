#Mandy and Viviana
#A: The __init__() function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
#it would just print John and his age with classing it as Person 1.
#We were correct because it did print John and his age. 

p2 = Person("Viviana", 22)

print(p2.name)
print(p2.age)

