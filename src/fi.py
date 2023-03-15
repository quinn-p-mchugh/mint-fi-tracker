"""Module for calculating financial metrics related to FIRE (Financial Independence/Retire Early)"""

from datetime import date

def __calc_savings_rate(date_start: date, date_end: date, pretax_contributions):
    """Calculate savings rate over a specified time period."""
    
    # "savings" = 401k contributions + IRA contributions + mortgage principle + college savings + taxable investments + HSA savings + other sabings accounts
    total_savings = 
    income = __get_income(date_start, date_end)
    expenses = __get_expenses(date_start, date_end)
    
    net_income = income - expenses
    
    savings_rate = total_savings / net_income
    
    
    
def __get_income(date_start: date, date_end: date):
    """Calculate income for a specified time period (via MINT transactions)."""
    


def years_till_fi(savings_rate, ):
    pass