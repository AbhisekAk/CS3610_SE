from zoo.IAnimalClass import IAnimal

class Penguin(IAnimal):
    def __init__(self):
        self.__name = "Penguin"

    def say(self):
        return f"{self.__name} is Honk-honking"
