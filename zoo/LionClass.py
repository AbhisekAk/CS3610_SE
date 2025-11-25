from zoo.IAnimalClass import IAnimal

'''
The Lion Concrete Class implements the Animal interface
'''
class Lion(IAnimal):
    def __init__(self):
        self.__name = "Lion"

    def say(self):
        return f"{self.__name} is Roaring"
