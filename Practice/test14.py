#Inheritance
class Animal:
    def walk(self):
        print("Walk")


class Dog(Animal):
    def bark(self):
        print("Bark")


class Cat(Animal):
    def meow(self):
        print("Meow")


dog = Dog()
dog.walk()
dog.bark()
cat = Cat()
cat.walk()
cat.meow()

