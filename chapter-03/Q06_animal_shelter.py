import unittest
from collections import deque


class AnimalShelter:
    def __init__(self):
        self.dogs = deque([])
        self.cats = deque([])

    def enqueue(self, animal):
        if animal.__class__ == Cat:
            self.cats.appendleft(animal)
        else:
            self.dogs.appendleft(animal)

    def dequeue_dog(self):
        return self.dogs.pop()

    def dequeue_cat(self):
        return self.cats.pop()

    def dequeue_any(self):
        if not self.cats or self.dogs[-1].time_rescued < self.cats[-1].time_rescued:
            return self.dequeue_dog()
        return self.dequeue_cat()


class Animal:
    def __init__(self, name, time_rescued):
        self.name = name
        self.time_rescued = time_rescued


class Cat(Animal):
    pass


class Dog(Animal):
    pass


class Unittest(unittest.TestCase):
    def test_animal_shelter(self):
        shelter = AnimalShelter()
        shelter.enqueue(Cat("Garfield", 10))
        shelter.enqueue(Dog("Fluffy", 15))
        shelter.enqueue(Dog("Scooby", 20))
        shelter.enqueue(Cat("Simba", 22))
        self.assertEqual("Garfield", shelter.dequeue_cat().name)
        self.assertEqual("Fluffy", shelter.dequeue_dog().name)
        self.assertEqual("Scooby", shelter.dequeue_any().name)
        self.assertEqual("Simba", shelter.dequeue_cat().name)
