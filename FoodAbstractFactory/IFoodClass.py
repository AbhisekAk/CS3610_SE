from abc import ABC, abstractmethod

'''The Food Interface (Product)'''

class IFood(ABC):

    @abstractmethod
    def get_Description(self) -> str:
        pass

    @abstractmethod
    def get_Price(self) -> float:
        pass
    
    def get_calories(self)->float:
        pass
    
