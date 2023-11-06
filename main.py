from Classes import Dog, Cat

if __name__ == '__main__':
    dog = Dog("Chintu", "Dog")
    cat = Cat("Kutti", "Cat")

    print(f"{dog.name} says: {dog.speak()}")
    print(f"{cat.name} says: {cat.speak()}")
