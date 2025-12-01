# FinanceAdapter/ServicesClass.py

class TaxCalculatorCSVService:
    """
    External tax service (Adaptee).
    Returns CSV text for tax-related transactions.
    """

    def serviceMethod(self) -> str:
        # Very simple CSV format
        return (
            "source,amount,currency\n"
            "tax_refund,1200.50,CAD\n"
            "tax_penalty,-300.00,CAD\n"
            "hst_rebate,150.00,CAD\n"
        )


class AccountingXMLService:
    """
    External accounting service (Adaptee).
    Returns accounting data as XML text.
    """

    def serviceMethod(self) -> str:
        return """
<transactions>
    <transaction>
        <source>payroll</source>
        <amount>5000.00</amount>
        <currency>CAD</currency>
    </transaction>
    <transaction>
        <source>office_rent</source>
        <amount>-2000.00</amount>
        <currency>CAD</currency>
    </transaction>
    <transaction>
        <source>utilities</source>
        <amount>-500.00</amount>
        <currency>CAD</currency>
    </transaction>
</transactions>
"""


class CreditAuthorizationJSONService:
    """
    External credit service (Adaptee).
    Returns something that *looks like* JSON, but we will
    treat it as plain text, not as a dict.
    """

    def serviceMethod(self) -> str:
        # Just a JSON-like string; we won't parse as dict
        return """
{
  "transactions": [
    {"src": "credit_line", "value": 3000.0, "ccy": "CAD"},
    {"src": "credit_interest", "value": -150.0, "ccy": "CAD"},
    {"src": "card_fee", "value": -50.0, "ccy": "CAD"}
  ]
}
"""
