# HRBridgeFactory/PaymentImplementation.py

from abc import ABC, abstractmethod


class IPaymentImplementation(ABC):


    @abstractmethod
    def pay(self, employee_name: str, amount: float) -> str:
        pass

    def __str__(self):
        return f"{self.__class__}"


class BankTransferPayment(IPaymentImplementation):
    def pay(self, employee_name: str, amount: float) -> str:
        return f"[Bank] Paid {amount:.2f} to {employee_name} via bank transfer."


class ChequePayment(IPaymentImplementation):
    def pay(self, employee_name: str, amount: float) -> str:
        return f"[Cheque] Issued cheque of {amount:.2f} to {employee_name}."


class DigitalWalletPayment(IPaymentImplementation):
    def pay(self, employee_name: str, amount: float) -> str:
        return f"[Wallet] Transferred {amount:.2f} to {employee_name}'s digital wallet."
