from cashflow import Inflow, Outflow
from dateutil.rrule import rrule, MONTHLY
from datetime import date, timedelta

today = date.today()
taxes = [
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
]
