import re
import random


def generate_random_cash_flow_statement(company_name):
    """Generates a random simplified cash flow statement."""
    data = {"Company": company_name, "Type": "Cash Flow Statement"}

    net_income = round(random.uniform(10, 100), 2)
    depreciation_amortization = round(net_income * random.uniform(0.1, 0.3), 2)
    change_in_working_capital = round(net_income * random.uniform(-0.2, 0.2), 2)
    cash_from_operations = round(
        net_income + depreciation_amortization + change_in_working_capital, 2
    )
    capital_expenditures = round(
        -abs(cash_from_operations) * random.uniform(0.2, 0.5), 2
    )
    proceeds_from_asset_sales = round(
        abs(capital_expenditures) * random.uniform(0.1, 0.3), 2
    )
    cash_from_investing = round(capital_expenditures + proceeds_from_asset_sales, 2)
    proceeds_from_debt = round(random.uniform(0, 50), 2)
    repayment_of_debt = round(-random.uniform(0, 30), 2)
    dividends_paid = round(-abs(net_income) * random.uniform(0.05, 0.15), 2)
    cash_from_financing = round(
        proceeds_from_debt + repayment_of_debt + dividends_paid, 2
    )
    net_change_in_cash = round(
        cash_from_operations + cash_from_investing + cash_from_financing, 2
    )
    beginning_cash = round(random.uniform(20, 80), 2)
    ending_cash = round(beginning_cash + net_change_in_cash, 2)

    data["Net Income"] = net_income
    data["Depreciation & Amortization"] = depreciation_amortization
    data["Change in Working Capital"] = change_in_working_capital
    data["Cash from Operating Activities"] = cash_from_operations
    data["Capital Expenditures"] = capital_expenditures
    data["Proceeds from Asset Sales"] = proceeds_from_asset_sales
    data["Cash from Investing Activities"] = cash_from_investing
    data["Proceeds from Debt"] = proceeds_from_debt
    data["Repayment of Debt"] = repayment_of_debt
    data["Dividends Paid"] = dividends_paid
    data["Cash from Financing Activities"] = cash_from_financing
    data["Net Change in Cash"] = net_change_in_cash
    data["Beginning Cash"] = beginning_cash
    data["Ending Cash"] = ending_cash

    return data
