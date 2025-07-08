import re
import random

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