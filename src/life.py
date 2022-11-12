from datetime import date
from dateutil.rrule import rrule
import pandas as pd
from cashflow import CashFlow


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
