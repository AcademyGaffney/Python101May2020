class Alien:
    totalaliens = 0
    def __init__(self, name, planet):
        self.__name = name
        self.__planet = planet
        Alien.totalaliens += 1
        print(Alien.totalaliens);
    def greeting(self):
        print("Hello. I am " + self.__name + " from planet " + self.__planet)

a1 = Alien("Spock", "Vulcan")
a2 = Alien("Chewbacca", "Kashyyyk")

a1.greeting()
a2.greeting()
print(a1.totalaliens)
print(Alien.totalaliens)

print(a2._Alien__name)
