# HRBridgeFactory/PaymentCreator.py

from typing import Optional

from HRBridgeFactory.PaymentImplementation import (
    IPaymentImplementation,
    BankTransferPayment,
    ChequePayment,
    DigitalWalletPayment,
)

# Equivalent to myObjs in the notebook
myMethods = {
    "bank": BankTransferPayment,
    "cheque": ChequePayment,
    "wallet": DigitalWalletPayment,
}


class PaymentCreator:
    

    @staticmethod
    def create_object(name: str) -> Optional[IPaymentImplementation]:
        key = name.lower()
        try:
            if key in myMethods:
                return myMethods[key]()
            else:
                raise Exception(f"I can't create a payment handler for '{name}'")
        except Exception as e:
            print(e)
        return None
