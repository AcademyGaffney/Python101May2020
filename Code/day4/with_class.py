
class Dog:
    def __init__(self, name = 'Unnamed'):
        self.name = name

    def speak(self):
        print ("Woof")

    def __str__(self):
        return "I'm a dog named " + self.name

class Cat:
    def __init__(self, name = 'Unnamed'):
        self.name = name

    def speak(self):
        print ("Meow")


class Conure:

    def __init__(self, name = 'Unnamed'):
        self.name = name

    def speak(self):
        print ("SQUAWK")


animals = [Dog("Spot"), Cat("Muffin"), Conure("Lio")]


def all_talk(pets):
    for pet in pets:
        pet.speak()


all_talk(animals)

print(animals[0])
print(animals[1])

