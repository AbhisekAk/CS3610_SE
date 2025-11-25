from zoo.IAnimalClass import IAnimal

class WhiteBear(IAnimal):
    def __init__(self):
        self.__name = "White Bear"

    def say(self):
        return f"{self.__name} is Growling (Polar Bear)"
