"""CONTAINS ALL CALCULATION CODE FOR FinTem"""
from cent_helper import to_cent
from decimal import Decimal
transactions = [
    {"date": "2026-11-01", "amount": 5000, "type": "income", "category": "salary"},
    {"date": "2026-11-02", "amount": 1200, "type": "expense", "category": "food"},
    {"date": "2026-11-02", "amount": 800, "type": "expense", "category": "food"},
    {"date": "2026-11-03", "amount": 800, "type": "expense", "category": "transport"},
    {"date": "2026-11-04", "amount": 800, "type": "income", "category": "transport"},
]


""" TO GET TOTAL INCOME """
def total_income(txs):
    """This gives us the total spent on income till now"""
    return sum(t.get("amount",0) for t in txs if t.get("type") == "income")


""" TO GET TOTAL EXPENSES """
def total_expense(txs):
    return sum(t.get("amount",0) for t in txs if t.get("type") == "expense")
"T0 GET SPENDING BY CATEGORY"
def spending_by_category(txs):
    """Returns dictionary of categorized expenses"""
    category_totals = {}
    for t in txs:
        if t.get("type") == "expense":
            category = t.get("category")
            amount = t.get("amount")
            category_totals[category] = category_totals.get(category,0) + amount
    return category_totals
print(total_income(transactions))
print(total_expense(transactions))
print(spending_by_category(transactions))

print(to_cent(Decimal("25.555")))