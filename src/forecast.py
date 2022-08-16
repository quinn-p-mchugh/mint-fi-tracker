"""Module for creating financial independence forecast."""

from datetime import date, datetime, timedelta
from dateutil.rrule import rrule, MONTHLY, YEARLY, DAILY
import pandas as pd
import numpy as np
from typing import Optional
import plotly.express as px


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
            amount (float): The amount of cash.
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


class Life:
    """A person's life
    
    Attributes:
        date_born (date): The date the person was born (for calculating current age)
    """

    def __init__(self, date_born: date, cashflows: list[CashFlow] = []):
        self.age_current = self.calc_age(date_born)
        self.cashflows = cashflows

    @staticmethod
    def calc_age(birth_date: date) -> int:
        """Calculate age, given a birthday.

        Args:
            birth_date (date): The birth date from which age will be calculated.

        Returns:
            int: The age of the person.
        """
        today = date.today()
        birthday_happened = (today.month, today.day) < (
            birth_date.month,
            birth_date.day,
        )
        return today.year - birth_date.year - birthday_happened

    def generate_financial_forecast(self, date_start: date, date_end: date):
        """Generates a financial forecast based off of user-defined cashflows and
        existing funds.

        Args:
            date_start (date): The start date of the forecast
            date_end (date): The end date of the forecast
        """
        self.forecast = pd.DataFrame(
            index=pd.date_range(start=date_start, end=date_end, freq="D"),
            columns=["Net Cashflow", "Cashflows"],
        )
        self.forecast["Net Cashflow"] = 0
        self.forecast["Cashflows"] = [[] for i in range(len(self.forecast))]

        for date in self.forecast.index:
            for cashflow in self.cashflows:
                if date in cashflow.frequency:
                    self.forecast.loc[
                        pd.to_datetime(date), "Net Cashflow"
                    ] += (cashflow.sign * cashflow.amount)
                    """self.forecast.loc[pd.to_datetime(date), "Cashflows"] += [
                        cashflow
                    ]"""
                    if cashflow.annual_rate_of_return:
                        cashflow.amount += (
                            cashflow.amount * cashflow.annual_rate_of_return
                        )

        self.forecast["Cumulative Sum"] = self.forecast[
            "Net Cashflow"
        ].cumsum()
        print(self.forecast)

        return self.forecast


today = date.today()
cashflows2 = (
    [
        Inflow(
            name="Gross Pay",
            amount=9111.54,
            frequency=rrule(
                MONTHLY, dtstart=today, until=today + timedelta(days=365 * 20)
            ),
        ),
        Outflow(
            name="Federal Income Tax",
            amount=1039.52,
            frequency=rrule(
                MONTHLY, dtstart=today, until=today + timedelta(days=365 * 20)
            ),
        ),
        Outflow(
            name="Federal Medicare Tax",
            amount=126.98,
            frequency=rrule(
                MONTHLY, dtstart=today, until=today + timedelta(days=365 * 20)
            ),
        ),
        Outflow(
            name="PA Withholding Tax",
            amount=268.86,
            frequency=rrule(
                MONTHLY, dtstart=today, until=today + timedelta(days=365 * 20)
            ),
        ),
        Outflow(
            name="PA Unemployment Tax",
            amount=5.30,
            frequency=rrule(
                MONTHLY, dtstart=today, until=today + timedelta(days=365 * 20)
            ),
        ),
        Outflow(
            name="Federal Social Security Tax",
            amount=542.96,
            frequency=rrule(
                MONTHLY, dtstart=today, until=today + timedelta(days=365 * 20)
            ),
        ),
        Outflow(
            name="Federal Social Security Tax",
            amount=1625,
            frequency=rrule(
                MONTHLY, dtstart=today, until=today + timedelta(days=365 * 20)
            ),
        ),
        Inflow(
            name="401K",
            amount=1625,
            frequency=rrule(
                MONTHLY, dtstart=today, until=today + timedelta(days=365 * 20)
            ),
            compound_interest=True,
            annual_rate_of_return=0.05 / 12,
        ),
        Outflow(
            name="Rent",
            amount=550,
            frequency=rrule(
                MONTHLY, dtstart=today, until=today + timedelta(days=365 * 20)
            ),
        ),
    ],
)

cashflows = [
    Inflow(
        name="401K",
        amount=1625,
        frequency=rrule(
            MONTHLY, dtstart=today, until=today + timedelta(days=365 * 20)
        ),
        compound_interest=True,
        annual_rate_of_return=0.05 / 12,
    ),
]

life = Life(date(2022, 2, 12), cashflows=cashflows)
forecast = life.generate_financial_forecast(
    today, today + timedelta(days=365 * 20)
)

fig = px.line(
    forecast,
    x=forecast.index,
    y="Cumulative Sum",
    title="Financial Independence Forecast",
)
fig.show()
