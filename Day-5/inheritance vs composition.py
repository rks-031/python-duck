# Inheritance: A subclass inherits attributes and methods from a superclass. Is- a relationship.

# Example:
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.speak()  # Inherited
dog.bark()


# Composition: A class contains instances of other classes. Has-a relationship.

class Engine:
    def start(self):
        print("Engine starts")

print('\n')

class Car:
    def __init__(self):
        self.engine = Engine()  # Car has-an Engine

    def start(self):
        self.engine.start()
        print("Car starts")

car = Car()
car.start()
