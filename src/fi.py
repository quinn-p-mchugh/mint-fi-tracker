"""Module for calculating financial metrics related to FIRE (Financial Independence/Retire Early)"""

from datetime import date

def __calc_savings_rate(date_start: date, date_end: date, pretax_contributions):
    """Calculate savings rate over a specified time period."""
    
    # "savings" = 401k contributions + IRA contributions + mortgage principle + college savings + taxable investments + HSA savings + other sabings accounts
    total_savings = 
    income = __get_income(date_start, date_end)
    expenses = __get_expenses(date_start, date_end)
    
    net_income = income - expenses
    
    # saving rate= (savings+interest on investment) /(earning+interest on investment)
    savings_rate = total_savings / net_income
    
    """Income:

Income after taxes

Expenses:

Recurring expenses

Misc. expenses

Savings:

Savings

Investing

Savingsrate: Savingsrate= ((Savings + Investing) / Income )*100"""


I update an income statement with totals from each month.

The top part lists all sources of income. This employment income (net amount from pay statement), 401k contributions (both mine and employers, taken from investment statements), interest, gifts received, side income, etc. Enter a subtotal for all income from the month.

The bottom section is for expenses. Sub lines for things like car expenses, rent, groceries, etc. Enter a subtotal for all expenses from the month.

Savings rate = (total income - total expenses)/total income


---

I will say it is nice to have savings split into to categories: long term (e.i. retirement) and short term (such as an emergency fund, car fund, vacation fund, etc.). I like to understand what I’m truly saving, versus just planning to spend in the next few months or years.

---

There is no real standardized way. I have asked the question many times in this sub. In particular, there is no consensus on including or excluding taxes, mortgage principle, student loan principle, etc. or when to include 401k, employer contributions, etc.
    
    
---

I manually track account positions, income, saving, and spending. Then, my spreadsheet calculates monthly income, spending, saving, and savings rate. It also calculates monthly net worth, and then does month-to-month and YTD changes for all the values as well.

Then the it puts all the information together, and shows this information.


---

Metrics to Consider:
    
    Savings Rate
Assets Breakdown
Years until FI / RE
Days until FI (xx / 365) or % to FI

--- 

I track most of the other things folks mentioned, plus one I just think is fun. It's net worth per day. I find out how many days it's been since I graduated from college and started my first job and divide my net worth by that. It's pretty nice to see that it's been growing over time, and gives you a sense of what you gain (on average) every day that goes by.
    
def __get_income(date_start: date, date_end: date):
    """Calculate income for a specified time period (via MINT transactions)."""
    


def years_till_fi(savings_rate, ):
    pass

def work_days_saved()
    """In a sense, each day you work translates into a certain number of retirement days. This tab calculates the differential between "days of freedom per day worked" for a FIRE scenario vs a standard retire-at-65 scenario."""
    pass

def left_to_save()
    """Considers my current investments, year-end projection, how much remaining I expect to save, and tells me what return I need for the remainder of the year to hit my target."""
    pass

# Move to different module:
def age_of_money():
    """How many days goes between getting a paycheck and spending those dollars. See YNAB for more on this."""
    pass


def days_of_buffering():
    """Based on my recent spending and current savings, how long could I last if I lost my income? See YNAB for more on this."""
    pass