# FinanceAdapter/ForecastingModuleClass.py

from FinanceAdapter.BaseFinanceClientClass import BaseFinanceClient


class ForecastingModule:
    """
    Client in the Adapter pattern.

    It only depends on the BaseFinanceClient interface (Target),
    and receives back STRING summaries from adapters.
    """

    def __init__(self, finance_client: BaseFinanceClient) -> None:
        self._client = finance_client

    def summarize(self) -> None:
        """
        Ask the underlying client (adapter) for data and print the summary.
        """
        summary = self._client.get_data("")
        print(summary)
