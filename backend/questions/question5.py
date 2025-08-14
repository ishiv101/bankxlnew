import re
import random

'''
def generate_random_financial_statement(company_name):
    """Generates a random simplified financial statement."""
    statement_type = random.choice(["Income Statement", "Balance Sheet", "Cash Flows"])
    data = {"Company": company_name, "Type": statement_type}

    if statement_type == "Income Statement":
        data["Revenue"] = round(random.uniform(100, 1000), 2)
        data["Cost of Goods Sold"] = round(
            data["Revenue"] * random.uniform(0.4, 0.7), 2
        )
        data["Gross Profit"] = round(data["Revenue"] - data["Cost of Goods Sold"], 2)
        data["Operating Expenses"] = round(
            data["Gross Profit"] * random.uniform(0.1, 0.3), 2
        )
        data["Operating Income"] = round(
            data["Gross Profit"] - data["Operating Expenses"], 2
        )
        data["Interest Expense"] = round(
            data["Operating Income"] * random.uniform(0.01, 0.05), 2
        )
        data["Income Before Tax"] = round(
            data["Operating Income"] - data["Interest Expense"], 2
        )
        data["Income Tax"] = round(
            data["Income Before Tax"] * random.uniform(0.2, 0.3), 2
        )
        data["Net Income"] = round(data["Income Before Tax"] - data["Income Tax"], 2)
    elif statement_type == "Balance Sheet":
        data["Assets"] = round(random.uniform(200, 2000), 2)
        data["Current Assets"] = round(data["Assets"] * random.uniform(0.3, 0.6), 2)
        data["Non-Current Assets"] = round(data["Assets"] - data["Current Assets"], 2)
        data["Liabilities"] = round(data["Assets"] * random.uniform(0.2, 0.7), 2)
        data["Current Liabilities"] = round(
            data["Liabilities"] * random.uniform(0.4, 0.8), 2
        )
        data["Non-Current Liabilities"] = round(
            data["Liabilities"] - data["Current Liabilities"], 2
        )
        data["Equity"] = round(data["Assets"] - data["Liabilities"], 2)
    elif statement_type == "Cash Flows":
        data["Net Income"] = round(random.uniform(10, 100), 2)
        data["Depreciation & Amortization"] = round(
            data["Net Income"] * random.uniform(0.1, 0.3), 2
        )
        data["Change in Working Capital"] = round(
            data["Net Income"] * random.uniform(-0.2, 0.2), 2
        )
        data["Cash from Operations"] = round(
            data["Net Income"]
            + data["Depreciation & Amortization"]
            + data["Change in Working Capital"],
            2,
        )
        data["Capital Expenditures"] = round(
            -data["Cash from Operations"] * random.uniform(0.2, 0.5), 2
        )
        data["Cash from Investing"] = round(data["Capital Expenditures"], 2)
        data["Proceeds from Debt"] = round(random.uniform(0, 50), 2)
        data["Repayment of Debt"] = round(-random.uniform(0, 30), 2)
        data["Cash from Financing"] = round(
            data["Proceeds from Debt"] + data["Repayment of Debt"], 2
        )
        data["Net Change in Cash"] = round(
            data["Cash from Operations"]
            + data["Cash from Investing"]
            + data["Cash from Financing"],
            2,
        )

    return data

'''