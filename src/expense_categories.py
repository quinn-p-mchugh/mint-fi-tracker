from enum import Enum, auto


class SpendCat(Enum):
    VARIABLE = auto()
    FIXED = auto()
    DISCRETIONARY = auto()


CATEGORIES = {
    "Auto & Transport": {
        "Auto & Transport": SpendCat.VARIABLE,
        "Auto Insurance": SpendCat.FIXED,
        "Auto Payment": SpendCat.FIXED,
        "Gas & Fuel": SpendCat.VARIABLE,
        "Parking": SpendCat.VARIABLE,
        "Public Transportation": SpendCat.FIXED,
        "Ride Share": SpendCat.DISCRETIONARY,
        "Service & Parts": SpendCat.VARIABLE,
    },
    "Bills & Utilities": {
        "Bills & Utilities": SpendCat.VARIABLE,
        "Home Phone": SpendCat.FIXED,
        "Internet": SpendCat.FIXED,
        "Mobile Phone": SpendCat.FIXED,
        "Television": SpendCat.FIXED,
        "Utilities": SpendCat.VARIABLE,
        "Electricity": SpendCat.VARIABLE,
        "Gas": SpendCat.VARIABLE,
        "Water": SpendCat.VARIABLE,
    },
    "Business Services": {
        "Business Services": SpendCat.VARIABLE,
        "Advertising": SpendCat.DISCRETIONARY,
        "Legal": SpendCat.VARIABLE,
        "Office Supplies": SpendCat.VARIABLE,
        "Printing": SpendCat.VARIABLE,
        "Shipping": SpendCat.VARIABLE,
    },
    "Education": {
        "Education": SpendCat.VARIABLE,
        "Books & Supplies": SpendCat.VARIABLE,
        "Student Loan": SpendCat.FIXED,
        "Tuition": SpendCat.FIXED,
        "Courses": SpendCat.DISCRETIONARY,
        "Tests": SpendCat.VARIABLE,
    },
    "Entertainment": {
        "Entertainment": SpendCat.DISCRETIONARY,
        "Amusement": SpendCat.DISCRETIONARY,
        "Arts": SpendCat.DISCRETIONARY,
        "Movies & DVDs": SpendCat.DISCRETIONARY,
        "Music": SpendCat.DISCRETIONARY,
        "Newspapers & Magazines": SpendCat.DISCRETIONARY,
    },
    "Fees & Charges": {
        "Fees & Charges": SpendCat.VARIABLE,
        "ATM Fee": SpendCat.VARIABLE,
        "Bank Fee": SpendCat.VARIABLE,
        "Finance Charge": SpendCat.VARIABLE,
        "Late Fee": SpendCat.VARIABLE,
        "Service Fee": SpendCat.VARIABLE,
        "Trade Commissions": SpendCat.VARIABLE,
        "Membership Fee": SpendCat.FIXED,
    },
    "Financial": {
        "Financial Advisor": SpendCat.DISCRETIONARY,
        "Life Insurance": SpendCat.FIXED,
    },
    "Food & Dining": {
        "Food & Dining": SpendCat.DISCRETIONARY,
        "Alcohol & Bars": SpendCat.DISCRETIONARY,
        "Coffee Shops": SpendCat.DISCRETIONARY,
        "Fast Food": SpendCat.DISCRETIONARY,
        "Food Delivery": SpendCat.DISCRETIONARY,
        "Groceries": SpendCat.VARIABLE,
        "Restaurants": SpendCat.DISCRETIONARY,
    },
    "Gifts & Donations": {
        "Gifts & Donations": SpendCat.DISCRETIONARY,
        "Charity": SpendCat.DISCRETIONARY,
        "Gift": SpendCat.DISCRETIONARY,
    },
    "Health & Fitness": {
        "Dentist": SpendCat.VARIABLE,
        "Doctor": SpendCat.VARIABLE,
        "Eyecare": SpendCat.VARIABLE,
        "Gym": SpendCat.FIXED,
        "Health Insurance": SpendCat.FIXED,
        "Pharmacy": SpendCat.VARIABLE,
        "Sports": SpendCat.DISCRETIONARY,
    },
    "Home": {
        "Furnishings": SpendCat.DISCRETIONARY,
        "Home Improvement": SpendCat.VARIABLE,
        "Home Insurance": SpendCat.FIXED,
        "Home Services": SpendCat.DISCRETIONARY,
        "Home Supplies": SpendCat.VARIABLE,
        "Lawn & Garden": SpendCat.DISCRETIONARY,
        "Mortgage & Rent": SpendCat.FIXED,
    },
    "Income": {
        "Bonus",
        "Interest Income",
        "Paycheck",
        "Reimbursement",
        "Rental Income",
        "Returned Purchase",
    },
    "Investments": {
        "Buy",
        "Deposit",
        "Dividend & Cap Gains",
        "Sell",
        "Withdrawal",
    },
    "Kids": {
        "Kids": SpendCat.VARIABLE,
        "Allowance": SpendCat.FIXED,
        "Baby Supplies": SpendCat.VARIABLE,
        "Babysitter & Daycare": SpendCat.FIXED,
        "Child Support": SpendCat.FIXED,
        "Kids Activities": SpendCat.DISCRETIONARY,
        "Toys": SpendCat.DISCRETIONARY,
    },
    "Loans": {
        "Loan Fees and Charges": SpendCat.VARIABLE,
        "Loan Insurance": SpendCat.FIXED,
        "Loan Interest": SpendCat.FIXED,
        "Loan Payment": SpendCat.FIXED,
        "Loan Principal": SpendCat.FIXED,
    },
    "Misc Expenses": {"Misc Expenses": SpendCat.VARIABLE},
    "Personal Care": {
        "Personal Care": SpendCat.VARIABLE,
        "Hair": SpendCat.FIXED,
        "Laundry": SpendCat.FIXED,
        "Spa & Massage": SpendCat.DISCRETIONARY,
    },
    "Pets": {
        "Pet Food & Supplies": SpendCat.VARIABLE,
        "Pet Grooming": SpendCat.DISCRETIONARY,
        "Veterinary": SpendCat.VARIABLE,
    },
    "Shopping": {
        "Shopping": SpendCat.DISCRETIONARY,
        "Books": SpendCat.DISCRETIONARY,
        "Clothing": SpendCat.DISCRETIONARY,
        "Electronics & Software": SpendCat.DISCRETIONARY,
        "Hobbies": SpendCat.DISCRETIONARY,
        "Sporting Goods": SpendCat.DISCRETIONARY,
    },
    "Taxes": {
        "Taxes": SpendCat.FIXED,
        "Federal Tax": SpendCat.FIXED,
        "Local Tax": SpendCat.FIXED,
        "Property Tax": SpendCat.FIXED,
        "Sales Tax": SpendCat.FIXED,
        "State Tax": SpendCat.FIXED,
    },
    "Travel": {
        "Travel": SpendCat.DISCRETIONARY,
        "Air Travel": SpendCat.DISCRETIONARY,
        "Hotel": SpendCat.DISCRETIONARY,
        "Rental Car & Taxi": SpendCat.DISCRETIONARY,
        "Vacation": SpendCat.DISCRETIONARY,
    },
    "Uncategorized": {"Cash & ATM", "Check",},
}


def get_expense_categories_dict(categories):
    categories_to_exclude = ["Uncategorized", "Investments", "Income", "Taxes"]
    expense_categories = categories
    for category in categories_to_exclude:
        del expense_categories[category]
    return expense_categories


EXPENSE_CATEGORIES = get_expense_categories_dict(CATEGORIES)


def get_expense_categories():
    categories = []
    for value in EXPENSE_CATEGORIES.values():
        categories.extend(value.keys())
    return categories

