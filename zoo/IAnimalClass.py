from abc import ABC, abstractmethod

'''The Animal Interface (Product)'''

class IAnimal(ABC):

   
    @abstractmethod
    def say() -> str:
        """Each animal will implement how it 'speaks'."""
        pass
