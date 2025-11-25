from FoodAbstractFactory.IFoodFactoryClass import FoodFactory
from FoodAbstractFactory.VegBurgerClass import VegBurger
from FoodAbstractFactory.VegPizzaClass import VegPizza
from FoodAbstractFactory.VegNoodlesClass import VegNoodles

class VegFoodFactory(FoodFactory):

    def createBurger(self, price: int, calories: int, descr: str):
        return VegBurger(price, calories, descr)

    def createPizza(self, price: int, calories: int, size: str, descr: str):
        return VegPizza(price, calories, size, descr)

    def createNoodles(self, price: int, calories: int, descr: str):
        return VegNoodles(price, calories, descr)