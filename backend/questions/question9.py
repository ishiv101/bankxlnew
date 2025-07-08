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
