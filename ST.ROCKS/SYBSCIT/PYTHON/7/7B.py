class Animal:
    def __init__ (self, name):
        self.name = name
    
    def speak(self):
        pass
    
class Dog (Animal):
    def speak(self):
        return f"{self.name} says woof"
    
class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"

dog = Dog("Leo")
cat = Cat("Kitty")

print(dog.speak())
print(cat.speak())