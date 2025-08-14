'''''

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
    '''