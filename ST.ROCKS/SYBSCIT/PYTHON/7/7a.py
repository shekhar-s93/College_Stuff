class xyz:
    pass
class Std:
    types = "Student Data: "
    
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def speak(self):
        return f"{self.name} says Hello to you!"

std1 = Std("Suman", 4)
std2 = Std("Shekhar", 9)

print(std1.types)
print("Name: ",std2.name)
print("Age", std2.age)
print(std1.speak())