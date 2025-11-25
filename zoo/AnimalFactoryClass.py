
from zoo.LionClass import Lion
from zoo.ElephantClass import Elephant
from zoo.PenguinClass import Penguin
from zoo.WhiteBearClass import WhiteBear
from zoo.GrizzlyBearClass import GrizzlyBear
from zoo.MooseClass import Moose

class AnimalsFactory:

    @staticmethod
    def create_Animal(objType: str):
        
        try:
            t = objType.lower()
            if t == "lion":
                return Lion()
            elif t == "elephant":
                return Elephant()
            elif t == "penguin":
                return Penguin()
            elif t == "whitebear":
                return WhiteBear()
            elif t == "grizzlybear":
                return GrizzlyBear()
            elif t == "moose":
                return Moose()
            else:
                raise Exception(f"I can't create this animal type: {objType}")
        except Exception as e:
            print(e)
        return None
