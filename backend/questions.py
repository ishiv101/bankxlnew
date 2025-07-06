import re
import random


def process_input(user_input):
    """
    Checks if the user input contains the trigger phrase and provides random numbers
    for private equity calculations if it does.

    Returns:
        A string indicating whether the trigger was found and, if so,
        a message with random numbers. Otherwise, returns an empty string.
    """

    if re.search(r"given info about the company", user_input, re.IGNORECASE):
        # Generate random numbers for different calculations
        revenue_growth = round(random.uniform(0.05, 0.20), 2)  # 5% to 20%
        ebitda_margin = round(random.uniform(0.10, 0.30), 2)  # 10% to 30%
        exit_multiple = round(random.uniform(5.0, 12.0), 1)  # 5x to 12x
        discount_rate = round(random.uniform(0.08, 0.15), 2)  # 8% to 15%
        debt_amount_multiplier = round(
            random.uniform(0.5, 3.0), 1
        )  # 0.5x to 3x of EBITDA

        return (
            "Detected 'given info about the company'. Here are some numbers for your calculations:\n"
            f"- Revenue Growth Rate: {revenue_growth}\n"
            f"- EBITDA Margin: {ebitda_margin}\n"
            f"- Exit Multiple: {exit_multiple}x\n"
            f"- Discount Rate: {discount_rate}\n"
            f"- Debt Amount (as a multiple of EBITDA): {debt_amount_multiplier}x\n"
            "Remember these numbers are randomly generated for each instance."
        )
    return ""


import re
import random


def process_input(user_id, user_input, company_data):
    """
    Checks if the user input contains the trigger phrase "some capital" and,
    if so, provides random financial data for a random company to the specified user.


    Args:
        user_id: A unique identifier for the user (e.g., an integer or string).
        user_input: The string input from the user.
        company_data: A dictionary where keys are company names and values are
                      dictionaries of financial data (this will be randomly chosen).


    Returns:
        A string indicating whether the trigger was found and, if so,
        a message with random financial data for a random company.
        Otherwise, returns an empty string.
    """
    if re.search(r"some capital", user_input, re.IGNORECASE):
        # Choose a random company
        random_company = random.choice(list(company_data.keys()))
        financial_data = company_data[random_company]

        return (
            f"User {user_id} triggered 'some capital'. Here is random financial data for {random_company}:\n"
            f"- Revenue: ${financial_data['revenue']:.2f} million\n"
            f"- Net Income: ${financial_data['net_income']:.2f} million\n"
            f"- Total Assets: ${financial_data['total_assets']:.2f} million\n"
            f"- Total Debt: ${financial_data['total_debt']:.2f} million\n"
            f"- Equity: ${financial_data['equity']:.2f} million\n"
            f"Use this data for your financial calculations."
        )
    return ""


def process_input(user_id, user_input, company_names):
    """
    Checks if the user input contains the trigger phrase "some %" and,
    if so, provides random percentage-based financial data for a random company
    to the specified user.


    Args:
        user_id: A unique identifier for the user (e.g., an integer or string).
        user_input: The string input from the user.
        company_names: A list of company names to choose from randomly.


    Returns:
        A string indicating whether the trigger was found and, if so,
        a message with random percentage-based financial data for a random company.
        Otherwise, returns an empty string.
    """
    if re.search(r"some %", user_input, re.IGNORECASE):
        # Choose a random company
        random_company = random.choice(company_names)

        # Generate random percentage-based financial data
        gross_margin = round(random.uniform(0.40, 0.80), 2)  # 40% to 80%
        operating_margin = round(random.uniform(0.10, 0.40), 2)  # 10% to 40%
        net_profit_margin = round(random.uniform(0.05, 0.25), 2)  # 5% to 25%
        revenue_growth_rate = round(random.uniform(-0.05, 0.20), 2)  # -5% to 20%
        cost_of_goods_sold_percent = round(1 - gross_margin, 2)
        operating_expenses_percent = round(gross_margin - operating_margin, 2)

        return (
            f"User {user_id} triggered 'some %'. Here is random percentage-based financial data for {random_company}:\n"
            f"- Gross Margin: {gross_margin * 100:.2f}%\n"
            f"- Operating Margin: {operating_margin * 100:.2f}%\n"
            f"- Net Profit Margin: {net_profit_margin * 100:.2f}%\n"
            f"- Revenue Growth Rate: {revenue_growth_rate * 100:.2f}%\n"
            f"- Cost of Goods Sold (as % of Revenue): {cost_of_goods_sold_percent * 100:.2f}%\n"
            f"- Operating Expenses (as % of Revenue): {operating_expenses_percent * 100:.2f}%\n"
            f"Use this data for your financial calculations."
        )
    return ""


import re
import random


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


def process_input(user_id, user_input, company_names):
    """
    Checks if the user input contains the trigger phrase "selected" and,
    if so, provides a random financial statement for a random company
    to the specified user.


    Args:
        user_id: A unique identifier for the user (e.g., an integer or string).
        user_input: The string input from the user.
        company_names: A list of company names to choose from randomly.


    Returns:
        A string indicating whether the trigger was found and, if so,
        a message with a random financial statement.
        Otherwise, returns an empty string.
    """
    if re.search(r"selected", user_input, re.IGNORECASE):
        # Choose a random company
        random_company = random.choice(company_names)

        # Generate a random financial statement
        financial_statement = generate_random_financial_statement(random_company)

        output_message = f"User {user_id} triggered 'selected'. Here is a random {financial_statement['Type']} for {financial_statement['Company']}:\n"
        for key, value in financial_statement.items():
            if key not in ["Company", "Type"]:
                output_message += f"- {key}: ${value:.2f} million\n"
        output_message += "Use this statement for your financial calculations."
        return output_message
    return ""


import re
import random


def generate_random_financial_statement(company_name, statement_type):
    """Generates a random simplified financial statement of a given type."""
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


def process_input(user_id, user_input, company_names):
    """
    Checks if the user input contains the trigger phrase "Given all 3 statements" and,
    if so, provides randomly generated Income Statement, Balance Sheet, and Cash Flows
    for a random company to the specified user.


    Args:
        user_id: A unique identifier for the user (e.g., an integer or string).
        user_input: The string input from the user.
        company_names: A list of company names to choose from randomly.


    Returns:
        A string indicating whether the trigger was found and, if so,
        a message with all three randomly generated financial statements.
        Otherwise, returns an empty string.
    """
    if re.search(r"Given all 3 statements", user_input, re.IGNORECASE):
        # Choose a random company
        random_company = random.choice(company_names)

        # Generate all three financial statements
        income_statement = generate_random_financial_statement(
            random_company, "Income Statement"
        )
        balance_sheet = generate_random_financial_statement(
            random_company, "Balance Sheet"
        )
        cash_flow_statement = generate_random_financial_statement(
            random_company, "Cash Flows"
        )

        output_message = f"User {user_id} triggered 'Given all 3 statements'. Here are the financial statements for {random_company}:\n\n"

        # Format and add Income Statement
        output_message += f"--- Income Statement ---\n"
        for key, value in income_statement.items():
            if key not in ["Company", "Type"]:
                output_message += f"- {key}: ${value:.2f} million\n"
        output_message += "\n"

        # Format and add Balance Sheet
        output_message += f"--- Balance Sheet ---\n"
        for key, value in balance_sheet.items():
            if key not in ["Company", "Type"]:
                output_message += f"- {key}: ${value:.2f} million\n"
        output_message += "\n"

        # Format and add Cash Flow Statement
        output_message += f"--- Cash Flow Statement ---\n"
        for key, value in cash_flow_statement.items():
            if key not in ["Company", "Type"]:
                output_message += f"- {key}: ${value:.2f} million\n"
        output_message += "\nUse these statements for your financial calculations."

        return output_message
    return ""


def process_input(user_id, user_input, company_names):
    """
    Checks if the user input contains the trigger phrase "some $" and,
    if so, provides random monetary-based financial data for a random company
    to the specified user.


    Args:
        user_id: A unique identifier for the user (e.g., an integer or string).
        user_input: The string input from the user.
        company_names: A list of company names to choose from randomly.


    Returns:
        A string indicating whether the trigger was found and, if so,
        a message with random monetary financial data for a random company.
        Otherwise, returns an empty string.
    """
    if re.search(r"some \$", user_input, re.IGNORECASE):
        # Choose a random company
        random_company = random.choice(company_names)

        # Generate random monetary financial data (in millions)
        revenue = round(random.uniform(50, 1000), 2)
        cost_of_goods_sold = round(revenue * random.uniform(0.4, 0.7), 2)
        operating_expenses = round(revenue * random.uniform(0.1, 0.3), 2)
        net_income = round(revenue * random.uniform(0.05, 0.20), 2)
        total_assets = round(random.uniform(100, 2000), 2)
        total_liabilities = round(total_assets * random.uniform(0.2, 0.7), 2)
        equity = round(total_assets - total_liabilities, 2)
        cash_flow_from_operations = round(net_income * random.uniform(0.8, 1.2), 2)
        capital_expenditures = round(
            -cash_flow_from_operations * random.uniform(0.1, 0.4), 2
        )

        return (
            f"User {user_id} triggered 'some $'. Here is random monetary financial data for {random_company} (in millions):\n"
            f"- Revenue: ${revenue:.2f}\n"
            f"- Cost of Goods Sold: ${cost_of_goods_sold:.2f}\n"
            f"- Operating Expenses: ${operating_expenses:.2f}\n"
            f"- Net Income: ${net_income:.2f}\n"
            f"- Total Assets: ${total_assets:.2f}\n"
            f"- Total Liabilities: ${total_liabilities:.2f}\n"
            f"- Equity: ${equity:.2f}\n"
            f"- Cash Flow from Operations: ${cash_flow_from_operations:.2f}\n"
            f"- Capital Expenditures: ${capital_expenditures:.2f}\n"
            f"Use this data for your financial calculations."
        )
    return ""


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


def process_input(user_id, user_input, company_names):
    """
    Checks if the user input contains the trigger phrase "Given a cash flow statement" and,
    if so, provides a randomly generated cash flow statement for a random company
    to the specified user.


    Args:
        user_id: A unique identifier for the user (e.g., an integer or string).
        user_input: The string input from the user.
        company_names: A list of company names to choose from randomly.


    Returns:
        A string indicating whether the trigger was found and, if so,
        a message with a random cash flow statement.
        Otherwise, returns an empty string.
    """
    if re.search(r"Given a cash flow statement", user_input, re.IGNORECASE):
        # Choose a random company
        random_company = random.choice(company_names)

        # Generate a random cash flow statement
        cash_flow_statement = generate_random_cash_flow_statement(random_company)

        output_message = f"User {user_id} triggered 'Given a cash flow statement'. Here is a random Cash Flow Statement for {cash_flow_statement['Company']}:\n"
        for key, value in cash_flow_statement.items():
            if key not in ["Company", "Type"]:
                output_message += f"- {key}: ${value:.2f} million\n"
        output_message += "Use this statement for your relevant financial calculations."
        return output_message
    return ""


import re
import random


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


def format_financial_statement(statement_data):
    """Formats a single financial statement for output."""
    output = f"--- {statement_data['Type']} ---\n"
    for key, value in statement_data.items():
        if key not in ["Company", "Type"]:
            output += f"- {key}: ${value:.2f} million\n"
    output += "\n"
    return output


def process_input(user_id, user_input, company_names):
    """
    Checks if the user input contains the trigger phrase "Given company financial statements" and,
    if so, provides randomly generated Income Statement, Balance Sheet, and Cash Flow Statement
    with enough information for DCF analysis, for a random company to the specified user.


    Args:
        user_id: A unique identifier for the user (e.g., an integer or string).
        user_input: The string input from the user.
        company_names: A list of company names to choose from randomly.


    Returns:
        A string indicating whether the trigger was found and, if so,
        a message with all three randomly generated financial statements.
        Otherwise, returns an empty string.
    """
    if re.search(r"Given company financial statements", user_input, re.IGNORECASE):
        # Choose a random company
        random_company = random.choice(company_names)

        # Generate all three financial statements
        all_statements = generate_random_financial_statements(random_company)

        output_message = f"User {user_id} triggered 'Given company financial statements'. Here are the financial statements for {all_statements['Company']} (in millions):\n\n"

        # Format and add Income Statement
        income_statement_data = {
            "Type": "Income Statement",
            **all_statements["Income Statement"],
        }
        output_message += format_financial_statement(income_statement_data)

        # Format and add Balance Sheet
        balance_sheet_data = {
            "Type": "Balance Sheet",
            **all_statements["Balance Sheet"],
        }
        output_message += format_financial_statement(balance_sheet_data)

        # Format and add Cash Flow Statement
        cash_flow_statement_data = {
            "Type": "Cash Flow Statement",
            **all_statements["Cash Flow Statement"],
        }
        output_message += format_financial_statement(cash_flow_statement_data)

        output_message += "Use these statements to perform your financial calculations, such as building a DCF model."
        return output_message
    return ""


# Example usage:
if __name__ == "__main__":
    company_list = [
        "FutureTech Inc.",
        "Global Consumer Goods",
        "Sustainable Energy Co.",
    ]
    user_ids = ["dcf_builder_1", "valuation_expert", "financial_modeler"]

    while True:
        for user_id in user_ids:
            user_input = input(f"[{user_id}] Enter text or type 'exit': ")
            if user_input.lower() == "exit":
                exit()
            output = process_input(user_id, user_input, company_list)
            if output:
                print(output)
            else:
                print(f"[{user_id}] Waiting for the financial statements...")


import re
import random


def generate_base_financial_statements(company_name):
    """Generates a base set of random financial statement data."""
    statements = {"Company": company_name}

    statements["Income Statement"] = {
        "Revenue": round(random.uniform(500, 1000), 2),
        "Cost of Goods Sold": round(random.uniform(300, 600), 2),
        "Operating Expenses": round(random.uniform(100, 300), 2),
        "Interest Expense": round(random.uniform(10, 50), 2),
        "Tax Expense": round(random.uniform(20, 80), 2),
        "Net Income": round(random.uniform(50, 150), 2),
    }

    statements["Balance Sheet"] = {
        "Cash": round(random.uniform(50, 200), 2),
        "Accounts Receivable": round(random.uniform(80, 250), 2),
        "Inventory": round(random.uniform(100, 300), 2),
        "Total Current Assets": None,  # Calculated later
        "Property, Plant, & Equipment": round(random.uniform(300, 700), 2),
        "Total Assets": None,  # Calculated later
        "Accounts Payable": round(random.uniform(60, 180), 2),
        "Short-Term Debt": round(random.uniform(30, 100), 2),
        "Total Current Liabilities": None,  # Calculated later
        "Long-Term Debt": round(random.uniform(200, 500), 2),
        "Total Liabilities": None,  # Calculated later
        "Equity": round(random.uniform(200, 600), 2),
        "Total Liabilities & Equity": None,  # Calculated later
    }
    statements["Balance Sheet"]["Total Current Assets"] = sum(
        statements["Balance Sheet"][key]
        for key in ["Cash", "Accounts Receivable", "Inventory"]
    )
    statements["Balance Sheet"]["Total Assets"] = (
        statements["Balance Sheet"]["Total Current Assets"]
        + statements["Balance Sheet"]["Property, Plant, & Equipment"]
    )
    statements["Balance Sheet"]["Total Current Liabilities"] = (
        statements["Balance Sheet"]["Accounts Payable"]
        + statements["Balance Sheet"]["Short-Term Debt"]
    )
    statements["Balance Sheet"]["Total Liabilities"] = (
        statements["Balance Sheet"]["Total Current Liabilities"]
        + statements["Balance Sheet"]["Long-Term Debt"]
    )
    statements["Balance Sheet"]["Total Liabilities & Equity"] = (
        statements["Balance Sheet"]["Total Liabilities"]
        + statements["Balance Sheet"]["Equity"]
    )

    statements["Cash Flow Statement"] = {
        "Net Income": statements["Income Statement"]["Net Income"],
        "Depreciation": round(random.uniform(20, 60), 2),
        "Change in Working Capital": round(random.uniform(-30, 30), 2),
        "Cash from Operations": None,  # Calculated later
        "Capital Expenditures": round(-random.uniform(40, 100), 2),
        "Cash from Investing": None,  # Calculated later
        "Proceeds from Debt": round(random.uniform(0, 50), 2),
        "Repayment of Debt": round(-random.uniform(0, 30), 2),
        "Cash from Financing": None,  # Calculated later
        "Net Change in Cash": None,  # Calculated later
    }
    statements["Cash Flow Statement"]["Cash from Operations"] = (
        statements["Cash Flow Statement"]["Net Income"]
        + statements["Cash Flow Statement"]["Depreciation"]
        + statements["Cash Flow Statement"]["Change in Working Capital"]
    )
    statements["Cash Flow Statement"]["Cash from Investing"] = statements[
        "Cash Flow Statement"
    ]["Capital Expenditures"]
    statements["Cash Flow Statement"]["Cash from Financing"] = (
        statements["Cash Flow Statement"]["Proceeds from Debt"]
        + statements["Cash Flow Statement"]["Repayment of Debt"]
    )
    statements["Cash Flow Statement"]["Net Change in Cash"] = (
        statements["Cash Flow Statement"]["Cash from Operations"]
        + statements["Cash Flow Statement"]["Cash from Investing"]
        + statements["Cash Flow Statement"]["Cash from Financing"]
    )

    return statements


def increase_financial_statement(base_statements, increase_factor):
    """Increases the amounts in the financial statements by a random factor."""
    increased_statements = {"Company": base_statements["Company"]}

    increased_statements["Income Statement"] = {
        key: round(value * increase_factor, 2)
        for key, value in base_statements["Income Statement"].items()
    }

    increased_statements["Balance Sheet"] = {
        key: (
            round(value * increase_factor, 2)
            if isinstance(value, (int, float))
            else value
        )
        for key, value in base_statements["Balance Sheet"].items()
    }
    # Recalculate totals after increase
    increased_statements["Balance Sheet"]["Total Current Assets"] = sum(
        increased_statements["Balance Sheet"][key]
        for key in ["Cash", "Accounts Receivable", "Inventory"]
    )
    increased_statements["Balance Sheet"]["Total Assets"] = (
        increased_statements["Balance Sheet"]["Total Current Assets"]
        + increased_statements["Balance Sheet"]["Property, Plant, & Equipment"]
    )
    increased_statements["Balance Sheet"]["Total Current Liabilities"] = (
        increased_statements["Balance Sheet"]["Accounts Payable"]
        + increased_statements["Balance Sheet"]["Short-Term Debt"]
    )
    increased_statements["Balance Sheet"]["Total Liabilities"] = (
        increased_statements["Balance Sheet"]["Total Current Liabilities"]
        + increased_statements["Balance Sheet"]["Long-Term Debt"]
    )
    increased_statements["Balance Sheet"]["Total Liabilities & Equity"] = (
        increased_statements["Balance Sheet"]["Total Liabilities"]
        + increased_statements["Balance Sheet"]["Equity"]
    )

    increased_statements["Cash Flow Statement"] = {
        key: round(value * increase_factor, 2)
        for key, value in base_statements["Cash Flow Statement"].items()
    }
    # Recalculate totals after increase
    increased_statements["Cash Flow Statement"]["Cash from Operations"] = (
        increased_statements["Cash Flow Statement"]["Net Income"]
        + increased_statements["Cash Flow Statement"]["Depreciation"]
        + increased_statements["Cash Flow Statement"]["Change in Working Capital"]
    )
    increased_statements["Cash Flow Statement"]["Cash from Investing"] = (
        increased_statements["Cash Flow Statement"]["Capital Expenditures"]
    )
    increased_statements["Cash Flow Statement"]["Cash from Financing"] = (
        increased_statements["Cash Flow Statement"]["Proceeds from Debt"]
        + increased_statements["Cash Flow Statement"]["Repayment of Debt"]
    )
    increased_statements["Cash Flow Statement"]["Net Change in Cash"] = (
        increased_statements["Cash Flow Statement"]["Cash from Operations"]
        + increased_statements["Cash Flow Statement"]["Cash from Investing"]
        + increased_statements["Cash Flow Statement"]["Cash from Financing"]
    )

    return increased_statements


def format_financial_statement(statement_data):
    """Formats a single financial statement for output."""
    output = f"--- {statement_data['Type']} ---\n"
    for key, value in statement_data.items():
        if key not in ["Company", "Type"]:
            output += f"- {key}: ${value:.2f} million\n"
    output += "\n"
    return output


def process_input(user_id, user_input, company_names):
    """
    Checks if the user input contains the trigger phrase "some amount" and,
    if so, provides randomly increased financial statements for a random company
    to the specified user.


    Args:
        user_id: A unique identifier for the user (e.g., an integer or string).
        user_input: The string input from the user.
        company_names: A list of company names to choose from randomly.


    Returns:
        A string indicating whether the trigger was found and, if so,
        a message with the increased financial statements.
        Otherwise, returns an empty string.
    """
    if re.search(r"some amount", user_input, re.IGNORECASE):
        # Choose a random company
        random_company = random.choice(company_names)

        # Generate base financial statements
        base_statements = generate_base_financial_statements(random_company)

        # Generate a random increase factor (e.g., 1.1 to 1.5 for 10% to 50% increase)
        increase_factor = round(random.uniform(1.1, 1.5), 2)
        increased_statements = increase_financial_statement(
            base_statements, increase_factor
        )

        output_message = f"User {user_id} triggered 'some amount'. Here are the increased financial statements for {increased_statements['Company']} (original amounts increased by {increase_factor - 1:.2%}):\n\n"

        # Format and add Income Statement
        income_statement_data = {
            "Type": "Income Statement",
            **increased_statements["Income Statement"],
        }
        output_message += format_financial_statement(income_statement_data)

        # Format and add Balance Sheet
        balance_sheet_data = {
            "Type": "Balance Sheet",
            **increased_statements["Balance Sheet"],
        }
        output_message += format_financial_statement(balance_sheet_data)

        # Format and add Cash Flow Statement
        cash_flow_statement_data = {
            "Type": "Cash Flow Statement",
            **increased_statements["Cash Flow Statement"],
        }
        output_message += format_financial_statement(cash_flow_statement_data)

        output_message += "Use these increased amounts for your financial calculations."
        return output_message
    return ""


import re
import random


def generate_depreciation_data():
    """Generates random data relevant to different depreciation methods."""
    asset_cost = round(random.uniform(10000, 1000000), 2)
    salvage_value = round(random.uniform(0.05, 0.2) * asset_cost, 2)
    useful_life_years = random.randint(3, 10)
    units_produced = random.randint(10000, 100000)
    total_units_expected = units_produced * random.randint(
        5, 15
    )  # Estimate total potential units

    return {
        "Asset Cost": asset_cost,
        "Salvage Value": salvage_value,
        "Useful Life (Years)": useful_life_years,
        "Units Produced This Year": units_produced,
        "Total Units Expected": total_units_expected,
    }


def analyze_depreciation_data(data):
    """Provides hints and calculations to help identify depreciation methods."""
    hints = [
        "Consider if the asset's usage is consistent over its life.",
        "Think about whether the asset's value decreases evenly each year.",
        "Is the asset's output a key factor in its wear and tear?",
    ]
    random.shuffle(hints)
    selected_hints = random.sample(hints, random.randint(1, len(hints)))

    straight_line_depreciation = (
        round(
            (data["Asset Cost"] - data["Salvage Value"]) / data["Useful Life (Years)"],
            2,
        )
        if data["Useful Life (Years)"] > 0
        else 0
    )
    units_of_production_depreciation = (
        round(
            (data["Asset Cost"] - data["Salvage Value"])
            / data["Total Units Expected"]
            * data["Units Produced This Year"],
            2,
        )
        if data["Total Units Expected"] > 0
        else 0
    )
    double_declining_balance_rate = (
        2 / data["Useful Life (Years)"] if data["Useful Life (Years)"] > 0 else 0
    )
    # Note: Calculating actual DDB for one year requires knowing accumulated depreciation,
    # so we'll just provide the rate for now.

    analysis = {
        "Hints": selected_hints,
        "Straight-Line Depreciation (per year, rough estimate)": straight_line_depreciation,
        "Units of Production Depreciation (this year, rough estimate)": units_of_production_depreciation,
        "Double-Declining Balance Rate (annual)": f"{double_declining_balance_rate * 100:.2f}%",
        "Considerations": [
            "Straight-line is simple and consistent.",
            "Units of production links depreciation to actual use.",
            "Double-declining balance is an accelerated method.",
        ],
    }
    return analysis


def process_input(user_id, user_input):
    """
    Checks if the user input contains the trigger phrase "some amount of depreciation" and,
    if so, provides random data and analysis to help identify depreciation methods.


    Args:
        user_id: A unique identifier for the user.
        user_input: The string input from the user.


    Returns:
        A string with depreciation data and analysis if the trigger is found,
        otherwise an empty string.
    """
    if re.search(r"some amount of depreciation", user_input, re.IGNORECASE):
        depreciation_data = generate_depreciation_data()
        analysis = analyze_depreciation_data(depreciation_data)

        output_message = f"User {user_id} triggered 'some amount of depreciation'. Here is some data to help you figure out the type and most efficient method:\n\n"
        for key, value in depreciation_data.items():
            output_message += f"- {key}: {value}\n"

        output_message += (
            "\nHere are some hints and initial calculations to consider:\n"
        )
        for hint in analysis["Hints"]:
            output_message += f"- Hint: {hint}\n"

        output_message += f"\n- Straight-Line Depreciation (approx. annual): ${analysis['Straight-Line Depreciation (per year, rough estimate)']}\n"
        output_message += f"- Units of Production Depreciation (approx. this year): ${analysis['Units of Production Depreciation (this year, rough estimate)']}\n"
        output_message += f"- Double-Declining Balance Rate (annual): {analysis['Double-Declining Balance Rate (annual)']}\n"

        output_message += "\nConsider these factors when choosing a method:\n"
        for consideration in analysis["Considerations"]:
            output_message += f"- {consideration}\n"

        output_message += "\nAnalyze this information to identify the most efficient depreciation method for this asset."
        return output_message
    return ""


import re
import random
from datetime import datetime, timedelta


def generate_random_stock_comp_expense():
    """Generates a random stock-based compensation expense amount."""
    return round(random.uniform(1, 50), 2)  # Random expense between $1M and $50M


def get_random_financial_statement_type():
    """Randomly selects one of the three financial statement types."""
    return random.choice(["Income Statement", "Balance Sheet", "Cash Flow Statement"])


def generate_impact_statement(statement_type, expense_amount):
    """Generates a description of the impact of stock-based compensation on a given statement."""
    impact = {}
    if statement_type == "Income Statement":
        impact["Description"] = (
            f"Stock-based compensation expense of ${expense_amount} million is recognized as an operating expense, reducing the company's profitability."
        )
        impact["Key Impacts"] = [
            f"- Operating Expenses: Increased by ${expense_amount} million.",
            f"- Pre-tax Income: Decreased by ${expense_amount} million.",
            f"- Net Income: Decreased by approximately ${expense_amount * (1 - random.uniform(0.2, 0.3)):.2f} million (assuming a random tax rate).",
        ]
    elif statement_type == "Balance Sheet":
        impact["Description"] = (
            "Stock-based compensation affects the balance sheet primarily through the increase in equity as options/shares vest and are exercised."
        )
        impact["Key Impacts"] = [
            f"- Equity (Contributed Capital): Increased by a non-cash amount related to the expensed compensation over the vesting period. The exact impact this period depends on the vesting schedule.",
            f"- Retained Earnings: Decreased by the net income reduction from the income statement.",
            "Note: The cash impact occurs upon exercise of stock options or vesting of restricted stock units (RSUs), which isn't directly captured by the expense recognition.",
        ]
    elif statement_type == "Cash Flow Statement":
        impact["Description"] = (
            "Stock-based compensation is a non-cash expense that is added back to net income in the operating activities section of the cash flow statement. The cash outflow occurs when options are exercised and shares are repurchased (if applicable)."
        )
        impact["Key Impacts"] = [
            f"- Net Income (Starting Point): Increased by the non-cash stock-based compensation expense of ${expense_amount} million.",
            "- Cash from Operating Activities: Increased by the add-back of this non-cash expense.",
            "Note: Cash outflow related to stock option exercises (if any) would be reflected in financing activities (as cash from the issuance of stock). Cash used for share repurchases (if any) would also be in financing activities.",
        ]
    return impact


def process_input(user_id, user_input, company_names):
    """
    Checks if the user input contains the trigger phrase "stock-based compensation" and,
    if so, provides a random stock-based compensation expense amount and its impact
    on a randomly selected financial statement for a random company to the user.


    Args:
        user_id: A unique identifier for the user.
        user_input: The string input from the user.
        company_names: A list of company names to choose from randomly.


    Returns:
        A string with the impact of stock-based compensation on a random financial
        statement if the trigger is found, otherwise an empty string.
    """
    if re.search(r"stock-based compensation", user_input, re.IGNORECASE):
        random_company = random.choice(company_names)
        expense_amount = generate_random_stock_comp_expense()
        statement_type = get_random_financial_statement_type()
        impact = generate_impact_statement(statement_type, expense_amount)

        output_message = f"User {user_id} triggered 'stock-based compensation' for {random_company}.\n"
        output_message += f"Let's look at the impact of a stock-based compensation expense of ${expense_amount} million on the **{statement_type}**:\n\n"
        output_message += f"{impact['Description']}\n"
        if "Key Impacts" in impact:
            output_message += "Key Impacts:\n"
            for item in impact["Key Impacts"]:
                output_message += f"- {item}\n"

        return output_message
    return ""


import re
import random


def generate_investment_data():
    """Generates random data for investment evaluation."""
    investment_name = (
        f"Project {chr(random.randint(65, 90))}"  # Random project name (A-Z)
    )
    initial_investment = round(random.uniform(100000, 1000000), 2)
    discount_rate = round(random.uniform(0.08, 0.15), 3)  # Cost of capital (8% to 15%)
    project_life_years = random.randint(5, 10)
    cash_flows = [
        round(
            random.uniform(0.1, 0.3)
            * initial_investment
            * (1 + random.uniform(-0.05, 0.1)),
            2,
        )
        for _ in range(project_life_years)
    ]  # Random cash flows with some growth/decline
    terminal_value_multiplier = round(
        random.uniform(5, 10), 1
    )  # Multiple of final year cash flow

    return {
        "Investment Name": investment_name,
        "Initial Investment": -initial_investment,
        "Discount Rate (Cost of Capital)": discount_rate,
        "Project Life (Years)": project_life_years,
        "Expected Annual Cash Flows": cash_flows,
        "Terminal Value Multiplier (Exit Multiple)": terminal_value_multiplier,
    }


def calculate_npv(cash_flows, discount_rate, initial_investment):
    """Calculates the Net Present Value (NPV) of an investment."""
    npv = initial_investment
    for i, cf in enumerate(cash_flows):
        npv += cf / (1 + discount_rate) ** (i + 1)
    return round(npv, 2)


def calculate_irr(cash_flows, initial_investment, iterations=100):
    """Calculates the Internal Rate of Return (IRR) using a numerical method."""
    rate_low = -0.5
    rate_high = 0.5
    for _ in range(iterations):
        mid_rate = (rate_low + rate_high) / 2
        npv = initial_investment
        for i, cf in enumerate(cash_flows):
            npv += cf / (1 + mid_rate) ** (i + 1)
        if npv > 0:
            rate_low = mid_rate
        else:
            rate_high = mid_rate
        if abs(npv) < 0.001:  # Tolerance for convergence
            return round(mid_rate * 100, 2)
    return "IRR could not be reliably calculated within the iterations."


def calculate_payback_period(cash_flows, initial_investment):
    """Calculates the payback period of an investment."""
    cumulative_cash_flow = -initial_investment
    payback_year = 0
    for i, cf in enumerate(cash_flows):
        cumulative_cash_flow += cf
        if cumulative_cash_flow >= 0:
            payback_year = i + 1
            break
    return payback_year if payback_year > 0 else "Never"


def process_input(user_id, user_input, company_names):
    """
    Checks if the user input contains the trigger phrase "given investment" and,
    if so, provides random investment data and basic evaluation metrics.


    Args:
        user_id: A unique identifier for the user.
        user_input: The string input from the user.
        company_names: A list of company names (can be used for context if needed).


    Returns:
        A string with investment data and evaluation metrics if the trigger is found,
        otherwise an empty string.
    """
    if re.search(r"given investment", user_input, re.IGNORECASE):
        investment_data = generate_investment_data()
        cash_flows_with_terminal = investment_data["Expected Annual Cash Flows"] + [
            investment_data["Expected Annual Cash Flows"][-1]
            * investment_data["Terminal Value Multiplier (Exit Multiple)"]
        ]
        npv = calculate_npv(
            cash_flows_with_terminal,
            investment_data["Discount Rate (Cost of Capital)"],
            investment_data["Initial Investment"],
        )
        irr = calculate_irr(
            investment_data["Expected Annual Cash Flows"],
            investment_data["Initial Investment"],
        )
        payback = calculate_payback_period(
            investment_data["Expected Annual Cash Flows"],
            investment_data["Initial Investment"],
        )

        output_message = f"User {user_id} triggered 'given investment'. Here is data for evaluating {investment_data['Investment Name']}:\n\n"
        for key, value in investment_data.items():
            if key == "Expected Annual Cash Flows":
                output_message += f"- {key} (Year 1 to {investment_data['Project Life (Years)']}): ${', $'.join(map(str, value))}\n"
            else:
                output_message += f"- {key}: {value}\n"

        output_message += f"\nBasic Investment Evaluation Metrics:\n"
        output_message += f"- Net Present Value (NPV): ${npv}\n"
        output_message += f"- Internal Rate of Return (IRR): {irr}%\n"
        output_message += f"- Payback Period: {payback} years\n"

        output_message += "\nConsider the NPV (should be positive), IRR (should be higher than the discount rate), and Payback Period (shorter is better) to assess if the investment is worth the risk."
        output_message += " Remember to also consider qualitative factors and the reliability of these estimates."
        return output_message
    return ""


import re

app = Flask(__name__)

MISTAKE_HINTS = {
    "unmatched_parentheses": "Check for missing or extra parentheses.",
    "invalid_characters": "Formula contains invalid characters. Stick to variables, numbers, and operators.",
    "consecutive_operators": "Consecutive operators detected. Review your formula.",
    "missing_operator": "Possible missing operator between numbers or variables.",
    "division_by_zero": "Division by zero risk detected.",
    "invalid_percentage": "Percentages should be between 0% and 100%.",
    "unrecognized_variable": "Unrecognized variable used. Verify spelling.",
}

ALLOWED_VARIABLES = [
    "Revenue",
    "COGS",
    "OperatingExpenses",
    "OperatingIncome",
    "EBITDA",
    "NetIncome",
    "GrossMargin",
    "EBITDAMargin",
    "NetMargin",
    "DiscountRate",
    "ExitMultiple",
    "DebtAmount",
    "RevenueGrowth",
    "CostOfGoodsSoldPercent",
    "OperatingExpensesPercent",
]


def check_formula():
    data = request.get_json()
    formula = data.get("formula", "")
    hints = []

    if formula.count("(") != formula.count(")"):
        hints.append(MISTAKE_HINTS["unmatched_parentheses"])
    if re.search(r"[^a-zA-Z0-9\+\-\*/\.\(\)\s]", formula):
        hints.append(MISTAKE_HINTS["invalid_characters"])
    if re.search(r"[\+\-\*/]{2,}", formula.replace("**", "")):
        hints.append(MISTAKE_HINTS["consecutive_operators"])
    if re.search(r"\d[a-zA-Z]", formula) or re.search(r"[a-zA-Z]\d", formula):
        hints.append(MISTAKE_HINTS["missing_operator"])
    if re.search(r"/0(?!\d)", formula):
        hints.append(MISTAKE_HINTS["division_by_zero"])

    # Variable validation
    tokens = re.findall(r"[a-zA-Z_]+", formula)
    for token in tokens:
        if token not in ALLOWED_VARIABLES:
            hints.append(f"{MISTAKE_HINTS['unrecognized_variable']} → '{token}'")

    if not hints:
        hints.append("✅ No mistakes detected. Formula looks good!")

    return {"hints": hints}


if __name__ == "__main__":
    app.run(debug=True)
