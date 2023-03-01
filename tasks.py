import random
from unidecode import unidecode
import json

def task1():
    out:str = "1. feladat: "
    for i in range(0,6):
        for j in range(0,random.randint(1,6)):
            out += "*"
        out += " "
    print(out)

def task2():
    print("2. feladat: ")
    inStr:str = input("írja be a szöveget: ")
    chunks:list = inStr.split(" ")
    for i in range(0,len(chunks)):
        chunks[i] = normalizeString(chunks[i])
        if i > 0:
            chunks[i] = chunks[i].capitalize()

    print("camelCase változata: " + "".join(chunks))



def normalizeString(inStr:str):
    return "".join(ch for ch in unidecode(inStr).lower() if ch.isalnum())

class Planet:
    def __init__(self, str):
        location, name, distance, direction, diameter, explorer, exploredYear = str.split(";")
        self.location = location
        self.name = name
        self.distance:int = int(distance)
        self.direction:int = int(direction)
        self.diameter:int = int(diameter)
        self.explorer = explorer
        self.exploredYear:int = int(exploredYear)

class PlanetEncoder(json.JSONEncoder):
    def default(self, obj):
            return {
                "location": obj.location,
                "name": obj.name,
                "distance": obj.distance,
                "direction": obj.direction,
                "diameter": obj.diameter,
                "explorer": obj.explorer,
                "exploredYear": obj.exploredYear
            }