# FinanceAdapter/clientFinance.py

from FinanceAdapter.ServicesClass import (
    TaxCalculatorCSVService,
    AccountingXMLService,
    CreditAuthorizationJSONService,
)
from FinanceAdapter.AdaptersClass import (
    TaxCalculatorAdapter,
    AccountingAdapter,
    CreditServiceAdapter,
)
from FinanceAdapter.ForecastingModuleClass import ForecastingModule


def runFinanceAdapterDemo() -> None:
    """
    Demonstration of the Adapter pattern for Task 1, written in the
    same spirit as your teacher's StructuralPatterns1Adapter example:
    - no dicts
    - simple strings and summaries
    """

    print("=== Tax CSV Adapter ===")
    tax_service = TaxCalculatorCSVService()
    tax_adapter = TaxCalculatorAdapter(tax_service)
    ForecastingModule(tax_adapter).summarize()

    print("\n=== Accounting XML Adapter ===")
    acc_service = AccountingXMLService()
    acc_adapter = AccountingAdapter(acc_service)
    ForecastingModule(acc_adapter).summarize()

    print("\n=== Credit JSON-like Adapter ===")
    cred_service = CreditAuthorizationJSONService()
    cred_adapter = CreditServiceAdapter(cred_service)
    ForecastingModule(cred_adapter).summarize()
