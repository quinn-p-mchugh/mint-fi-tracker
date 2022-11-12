from cashflow import Inflow, Outflow
from dateutil.rrule import rrule, MONTHLY
from datetime import date, timedelta

today = date.today()
retirement = [
    Inflow(
        name="401K",
        amount=1625,
        frequency=rrule(
            MONTHLY, dtstart=today, until=today + timedelta(days=365 * 20)
        ),
        compound_interest=True,
        annual_rate_of_return=0.05 / 12,
    )
]
