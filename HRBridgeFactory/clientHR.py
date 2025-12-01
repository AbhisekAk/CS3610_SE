# HRBridgeFactory/clientHR.py

from HRBridgeFactory.PaymentCreator import PaymentCreator
from HRBridgeFactory.EmployeeBridge import (
    HourlyEmployee,
    SalariedEmployee,
    ContractorEmployee,
)


def runHRBridgeDemo():

   

    method_names = ["bank", "cheque", "wallet"]
    implementations = []

    print("Creating Payment Implementations:")
    for name in method_names:
        impl = PaymentCreator.create_object(name)
        if impl:
            print("  ", impl)
            implementations.append(impl)

    bank_impl, cheque_impl, wallet_impl = implementations

    # ----- Bridge: Each employee gets an implementation -----

    emp1 = HourlyEmployee("Abhisek", 160, 25.0, bank_impl)
    emp2 = SalariedEmployee("Macey", 5000.0, cheque_impl)
    emp3 = ContractorEmployee("Joshua", 8000.0, wallet_impl)

    employees = [emp1, emp2, emp3]

    print("\n=== Running Payroll ===")
    for e in employees:
        print(e.pay())
    print("=== Payroll Complete ===")
