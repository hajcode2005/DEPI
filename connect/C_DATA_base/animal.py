
class Animal:
    def make_sound(self):
        raise NotImplementedError("Subclass must implement make_sound method")
    
    def describe(self):
        print(f"I am a {self.__class__.__name__}, and I am an animal.")


class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


class Cow(Animal):
    def make_sound(self):
        return "Moo!"

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.describe()
    print("Sound:", animal.make_sound())
    print("-" * 30)