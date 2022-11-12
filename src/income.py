from cashflow import Inflow, Outflow
from dateutil.rrule import rrule, MONTHLY
from datetime import date, timedelta

today = date.today()
income = [ Inflow(
            name="Gross Pay",
            amount=9111.54,
            frequency=rrule(
                MONTHLY, dtstart=today, until=today + timedelta(days=365 * 20)
            ),
        )]