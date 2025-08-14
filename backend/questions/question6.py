'''

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

'''''