
d1 = ["Spot", "Dog"]
c1 = ["Muffin", "Cat"]
b1 = ["Lio", "Conure"]

animals = [d1, c1, b1]

def alltalk(pets):
    for pet in pets:
        if pet[1] == "Dog":
            print("Wolf")
        if pet[1] == "Cat":
            print("Meow")
        if pet[1] == "Conure":
            print("SQUAWK")

alltalk(animals)