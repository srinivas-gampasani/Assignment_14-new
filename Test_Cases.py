import unittest
from Classes import Animal, Dog, Cat

class TestAnimal(unittest.TestCase):
    def test_animal_creation(self):
        animal = Animal("Hen", "Dog")
        self.assertEqual(animal.name, "Hen")
        self.assertEqual(animal.species, "Dog")

    def test_dog_speak(self):
        dog = Dog("Chintu", "Dog")
        self.assertEqual(dog.speak(), "Bow Bow!")

    def test_cat_speak(self):
        cat = Cat("Kutti", "Cat")
        self.assertEqual(cat.speak(), "Meow Meow!")

if __name__ == '__main__':
    unittest.main()
