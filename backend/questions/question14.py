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
