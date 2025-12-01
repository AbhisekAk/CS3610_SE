# FinanceAdapter/BaseFinanceClientClass.py

from abc import ABC


class BaseFinanceClient(ABC):
    """
    Existing class / Target in the Adapter pattern.

    The client expects to call get_data(text: str) and receive
    a processed STRING summary back.
    """

    def get_data(self, data: str) -> str:
        """
        Default behavior: just echo the input in a simple way.
        Adapters will OVERRIDE this method.
        """
        return f"[BaseFinanceClient] Received: {data}"
