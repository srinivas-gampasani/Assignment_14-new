class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

class Dog(Animal):
    def speak(self):
        return "Bow Bow!"

class Cat(Animal):
    def speak(self):
        return "Meow Meow!"