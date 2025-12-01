# FinanceAdapter/AdaptersClass.py

from FinanceAdapter.BaseFinanceClientClass import BaseFinanceClient
from FinanceAdapter.ServicesClass import (
    TaxCalculatorCSVService,
    AccountingXMLService,
    CreditAuthorizationJSONService,
)


class TaxCalculatorAdapter(BaseFinanceClient):
    """
    Adapter for TaxCalculatorCSVService.

    Converts CSV text into a *summary string* that the client understands.
    No dicts are used; everything is kept as simple strings, like in your
    teacher's Adapter example.
    """

    def __init__(self, service: TaxCalculatorCSVService) -> None:
        self._service = service

    def get_data(self, data: str = "") -> str:
        raw = self._service.serviceMethod()
        lines = [line.strip() for line in raw.strip().splitlines()]

        if not lines:
            return "[TaxAdapter] No tax records."

        header = lines[0]
        rows = lines[1:]  # data rows

        count = 0
        total = 0.0

        for row in rows:
            parts = row.split(",")
            if len(parts) != 3:
                continue
            source, amount_str, currency = parts
            try:
                amount = float(amount_str)
            except ValueError:
                continue
            count += 1
            total += amount

        return (
            f"[TaxAdapter] Processed {count} tax records "
            f"from CSV. Net amount = {total:.2f} CAD."
        )


class AccountingAdapter(BaseFinanceClient):
    """
    Adapter for AccountingXMLService.

    Parses the XML text just enough to count transactions and sum amounts,
    and returns a STRING summary (no dicts).
    """

    def __init__(self, service: AccountingXMLService) -> None:
        self._service = service

    def get_data(self, data: str = "") -> str:
        raw = self._service.serviceMethod()
        lines = [line.strip() for line in raw.strip().splitlines()]

        count = 0
        total = 0.0

        for line in lines:
            # Look for lines like: <amount>5000.00</amount>
            if "<amount>" in line and "</amount>" in line:
                start = line.find("<amount>") + len("<amount>")
                end = line.find("</amount>")
                amount_str = line[start:end].strip()
                try:
                    amount = float(amount_str)
                except ValueError:
                    continue
                count += 1
                total += amount

        return (
            f"[AccountingAdapter] Processed {count} accounting records "
            f"from XML. Net amount = {total:.2f} CAD."
        )


class CreditServiceAdapter(BaseFinanceClient):
    """
    Adapter for CreditAuthorizationJSONService.

    Treats the JSON-like response as plain text. It will:
    - count how many transactions appear
    - approximate a total by scanning for 'value' fields
    - return a STRING summary.

    Still no dicts; just simple string operations.
    """

    def __init__(self, service: CreditAuthorizationJSONService) -> None:
        self._service = service

    def get_data(self, data: str = "") -> str:
        raw = self._service.serviceMethod()
        lines = [line.strip() for line in raw.strip().splitlines()]

        count = 0
        total = 0.0

        for line in lines:
            # Look for snippets like: "value": 3000.0
            if '"value"' in line:
                # Try to grab the number after the colon
                parts = line.split(":")
                if len(parts) < 2:
                    continue
                amount_str = parts[1].strip().strip(",")
                try:
                    amount = float(amount_str)
                except ValueError:
                    continue
                count += 1
                total += amount

        return (
            f"[CreditAdapter] Processed {count} credit records "
            f"from JSON-like text. Net amount = {total:.2f} CAD."
        )
