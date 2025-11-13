import random
def say_hi(nombre = "caracol"):
    coin = random.random() > 0.5
    if coin:
        print("hi", nombre)
    else:
        print("bye", nombre)
