from FoodAbstractFactory.IFoodFactoryClass import FoodFactory
from FoodAbstractFactory.NonVegBurgerClass import NonVegBurger
from FoodAbstractFactory.NonVegCutletClass import NonVegCutlet
from FoodAbstractFactory.NonVegPizzaClass import NonVegPizza
from FoodAbstractFactory.NonVegNoodlesClass import NonVegNoodles

class NonVegFoodFactory(FoodFactory):

    def createBurger(self, price: int, calories: int, descr: str):
        return NonVegBurger(price, calories, descr)

    def createPizza(self, price: int, calories: int, size: str, descr: str):
        return NonVegPizza(price, calories, size, descr)

    def createNoodles(self, price: int, calories: int, descr: str):
        return NonVegNoodles(price, calories, descr)

    def createCutlet(self, price: int, calories: int, descr: str):
        return NonVegCutlet(price, calories, descr)



