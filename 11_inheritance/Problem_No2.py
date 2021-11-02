class Animal:
    animalType = "Mammel"

class Pets(Animal):
    colour = "White"

class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow bow")

d = Dog()
d.bark()
