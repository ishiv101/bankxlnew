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

print(process_input("hello"))