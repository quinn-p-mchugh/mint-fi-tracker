from cashflow import Inflow, Outflow
from dateutil.rrule import rrule, DAILY, MONTHLY
from datetime import date, timedelta

today = date.today()
home_price = 399900
down_payment = home_price * 0.20
home_purchase_date = date(2023, 1, 1)
home_end_date = home_purchase_date + timedelta(days=365 * 20)
home_cost = [
    Outflow(
        name="Down Payment",
        amount=down_payment,
        frequency=rrule(DAILY, dtstart=home_purchase_date, count=1),
    ),
    Outflow(
        name="Monthly Home Cost after Downpayment",
        amount=2187,
        frequency=rrule(
            MONTHLY, dtstart=home_purchase_date, until=home_end_date
        ),
    ),
]
rent = [
    Outflow(
        name="Rent",
        amount=550,
        frequency=rrule(MONTHLY, dtstart=today, until=home_purchase_date),
    )
]
housing = home_cost + rent


class Mortgage(Outflow):
    """A home mortgage.
    Base on: https://www.zillow.com/philadelphia-pa/home-values/
    
    Attributes:
        home_price (int): The final sale price of the home.
        insurance_cost_monthly (int): The monthly cost of home insurance.
        property_tax_rate_annual (float): The annual tax rate of the property.
        down_payment (int): The down payment on the mortgage.
        principle (int): The amount borrowed from a lender to buy the home, excluding the interest owed for borrowing.
    """

    class LoanPrograms(Enum):
        FIXED_30_YEAR = auto()
        FIXED_15_YEAR = auto()
        APR_5_YEAR = auto()

    def __init__(
        self,
        home_price: int,
        insurance_cost_monthly: int,
        property_tax_rate_annual: float,
        loan_program: LoanPrograms,
        down_payment: int = 0,
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.home_price = home_price
        self.insurance_cost_monthly = insurance_cost_monthly
        self.property_tax_rate_annual = property_tax_rate_annual
        self.down_payment = down_payment
        self.principle = home_price - down_payment
        self.loan_program = loan_program

        self.down_payment = Outflow
