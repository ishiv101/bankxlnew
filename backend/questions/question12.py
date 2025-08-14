import re
import random

'''
def generate_random_financial_statements(company_name):
    """Generates random simplified income statement, balance sheet, and cash flow statement."""
    statements = {"Company": company_name}

    # Income Statement
    statements["Income Statement"] = {
        "Revenue": round(random.uniform(500, 5000), 2),
        "Cost of Goods Sold": round(
            random.uniform(0.5, 0.7) * statements["Income Statement"]["Revenue"], 2
        ),
        "Gross Profit": None,  # Calculated below
        "Operating Expenses": round(
            random.uniform(0.1, 0.3) * statements["Income Statement"]["Revenue"], 2
        ),
        "Operating Income (EBIT)": None,  # Calculated below
        "Interest Expense": round(random.uniform(10, 100), 2),
        "Income Before Tax": None,  # Calculated below
        "Income Tax Expense": None,  # Calculated below
        "Net Income": None,  # Calculated below
    }
    statements["Income Statement"]["Gross Profit"] = round(
        statements["Income Statement"]["Revenue"]
        - statements["Income Statement"]["Cost of Goods Sold"],
        2,
    )
    statements["Income Statement"]["Operating Income (EBIT)"] = round(
        statements["Income Statement"]["Gross Profit"]
        - statements["Income Statement"]["Operating Expenses"],
        2,
    )
    statements["Income Statement"]["Income Before Tax"] = round(
        statements["Income Statement"]["Operating Income (EBIT)"]
        - statements["Income Statement"]["Interest Expense"],
        2,
    )
    statements["Income Statement"]["Income Tax Expense"] = round(
        random.uniform(0.2, 0.3) * statements["Income Statement"]["Income Before Tax"],
        2,
    )
    statements["Income Statement"]["Net Income"] = round(
        statements["Income Statement"]["Income Before Tax"]
        - statements["Income Statement"]["Income Tax Expense"],
        2,
    )

    # Balance Sheet
    total_assets = round(random.uniform(1000, 10000), 2)
    current_assets = round(random.uniform(0.3, 0.6) * total_assets, 2)
    non_current_assets = round(total_assets - current_assets, 2)
    total_liabilities = round(random.uniform(0.2, 0.7) * total_assets, 2)
    current_liabilities = round(random.uniform(0.4, 0.8) * total_liabilities, 2)
    non_current_liabilities = round(total_liabilities - current_liabilities, 2)
    equity = round(total_assets - total_liabilities, 2)

    statements["Balance Sheet"] = {
        "Current Assets": current_assets,
        "Non-Current Assets": non_current_assets,
        "Total Assets": total_assets,
        "Current Liabilities": current_liabilities,
        "Non-Current Liabilities": non_current_liabilities,
        "Total Liabilities": total_liabilities,
        "Equity": equity,
    }

    # Cash Flow Statement (simplified, direct method for operating)
    net_income_cf = statements["Income Statement"]["Net Income"]
    depreciation = round(random.uniform(0.05, 0.15) * total_assets, 2)
    change_in_working_capital = round(
        random.uniform(-0.05, 0.05) * statements["Income Statement"]["Revenue"], 2
    )
    capex = round(-random.uniform(0.05, 0.1) * total_assets, 2)
    debt_issued = round(random.uniform(0, 0.1) * total_assets, 2)
    debt_repaid = round(-random.uniform(0, 0.05) * total_assets, 2)

    statements["Cash Flow Statement"] = {
        "Net Income": net_income_cf,
        "Depreciation & Amortization": depreciation,
        "Change in Working Capital": change_in_working_capital,
        "Cash from Operating Activities": round(
            net_income_cf + depreciation + change_in_working_capital, 2
        ),
        "Capital Expenditures": capex,
        "Cash from Investing Activities": capex,
        "Proceeds from Debt Issuance": debt_issued,
        "Repayment of Debt": debt_repaid,
        "Cash from Financing Activities": round(debt_issued + debt_repaid, 2),
        "Net Change in Cash": None,  # Calculated below
        "Beginning Cash": round(random.uniform(50, 200), 2),
    }
    statements["Cash Flow Statement"]["Net Change in Cash"] = round(
        statements["Cash Flow Statement"]["Cash from Operating Activities"]
        + statements["Cash Flow Statement"]["Cash from Investing Activities"]
        + statements["Cash Flow Statement"]["Cash from Financing Activities"],
        2,
    )
    statements["Cash Flow Statement"]["Ending Cash"] = round(
        statements["Cash Flow Statement"]["Beginning Cash"]
        + statements["Cash Flow Statement"]["Net Change in Cash"],
        2,
    )

    return statements
    '''