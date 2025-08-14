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

