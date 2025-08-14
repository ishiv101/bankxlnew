
''''
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

    
    '''