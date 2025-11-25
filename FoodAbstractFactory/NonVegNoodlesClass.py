from FoodAbstractFactory.IFoodClass import IFood

class NonVegNoodles(IFood):
    def __init__(self, price: int, calories: int, descr: str) -> None:
        self._price = price
        self._calories = calories
        self._descr = descr

    def get_Price(self):
        return self._price

    def get_Description(self):
        return f"{self._descr} (NonVeg Noodles, {self._calories} cals, ${self._price})"
