# HRBridgeFactory/EmployeeBridge.py

from abc import ABC, abstractmethod
from HRBridgeFactory.PaymentImplementation import IPaymentImplementation


# ===== Abstraction =====
class IEmployee(ABC):
    """
    Abstraction in the Bridge pattern.
    Holds reference to a payment implementation.
    """

    def __init__(self, name: str, payment_impl: IPaymentImplementation) -> None:
        self._name = name
        self._payment_impl = payment_impl

    @abstractmethod
    def calculate_salary(self) -> float:
        pass

    def pay(self) -> str:
        amount = self.calculate_salary()
        return self._payment_impl.pay(self._name, amount)


# ===== Refined Abstractions =====
class HourlyEmployee(IEmployee):
    def __init__(self, name: str, hours: float, rate: float, impl: IPaymentImplementation):
        super().__init__(name, impl)
        self._hours = hours
        self._rate = rate

    def calculate_salary(self) -> float:
        return self._hours * self._rate


class SalariedEmployee(IEmployee):
    def __init__(self, name: str, monthly_salary: float, impl: IPaymentImplementation):
        super().__init__(name, impl)
        self._salary = monthly_salary

    def calculate_salary(self) -> float:
        return self._salary


class ContractorEmployee(IEmployee):
    def __init__(self, name: str, project_fee: float, impl: IPaymentImplementation):
        super().__init__(name, impl)
        self._fee = project_fee

    def calculate_salary(self) -> float:
        return self._fee
