"""Module for creating financial independence forecast."""

from dateutil.rrule import rrule
from typing import Optional


class CashFlow:
    def __init__(
        self,
        name: str,
        amount: float,
        frequency: Optional[rrule],
        compound_interest: bool = False,
        annual_rate_of_return: Optional[float] = None,
        description: Optional[str] = None,
    ):
        """_summary_

        _extended_summary_

        Args:
            name (str): _description_
            amount (float): The amount of cash flowing in or out for each frequency cycle.
            frequency (rrule): How frequent the cashflow occurs. If None, assume it occurs once.
            compound_interest (bool, optional): Whether or not the cashflow is affected by compound interest
            description (str, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        """
        self.name = name
        self.amount = amount
        self.description = description
        self.frequency = frequency
        self.compound_interest = compound_interest
        self.annual_rate_of_return = annual_rate_of_return


class Inflow(CashFlow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sign = 1


class Outflow(CashFlow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sign = -1
