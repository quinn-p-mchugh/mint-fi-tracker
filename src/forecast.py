"""Module for creating financial independence forecast."""

from datetime import date, timedelta
from dateutil import rrule
from pandas import DataFrame
from typing import Optional

class CashFlow():

    def __init__(self, name: str, t1: date, t2: date, recurring = False, description: str = None):
        """_summary_

        _extended_summary_

        Args:
            name (str): _description_
            t1 (date): The date the cash flow takes effect.
            t2 (date): The date the cash flow terminates.
            recurring (bool, optional): _description_. Defaults to False.
            description (str, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        """
        self.name = name
        self.description = description
        self.recurring = recurring
        self.t1 = t1
        self.t2 = t2



class Inflow(CashFlow):
    
    def __init__(self, name: str, t1: date, t2: date, recurring = False, description: Optional[str] = None, *args, **kwargs):
        super.__init__(*args, **kwargs)
        self.sign = 1


class Outflow(CashFlow):

    def __init__(self, name: str, amount: float, frequency:rrule, applied t1: date, t2: date, recurring = False, description: Optional[str] = None, *args, **kwargs):
        super.__init__(*args, **kwargs)
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

    def generate_financial_forecast(self, t1: date, t2: date):
        """Generates a financial forecast based off of user-defined cashflows and
        existing funds.

        Args:
            t1 (date): The start date of the forecast
            t2 (date): The end date of the forecast
        """
        self.forecast = DataFrame(columns = ["Year", "Month", "Date", "Running Total", "Net Cashflow", "Cashflows"])
        for dt in rrule.rrule(rrule.MONTHLY, dtstart=t1, until=t2):
            for cashflow in self.cashflows:
                if cashflow.t1.month() <= dt.month() <= cashflow.t2.month():
                    cashflow.sign
                    
                

life = Life(date(2022, 2, 12), [
    Outflow(name="Rent", )
])
today = date.today()
life.generate_financial_forecast(today, today + timedelta(days=365*50))