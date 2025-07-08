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

