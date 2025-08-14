import re
import random
from question7 import generate_random_financial_statement1

# Asks user to calculate Year 1 EBITDA and Acquisition Debt based on generated financial statements

def process_input1(user_input):
    print("\nPlease calculate:")
    print("1. Year 1 EBITDA")
    print("2. Acquisition Debt\n")

    requested_statements = set()
    max_statements = {"Income Statement", "Balance Sheet", "Cash Flows"}

    while True:
        request = input("Do you request a financial statement Yes or No? :").strip()

        if request.lower() == "yes":
            if requested_statements == max_statements:
                print("You have requested all available financial statements.")
                continue

            statement_type = input("Which of the three financial statements (Income Statement, Balance Sheet, or Cash Flows) do you request?: ").strip()

            if statement_type not in max_statements:
                print("Invalid statement type. Please choose from Income Statement, Balance Sheet, or Cash Flows.")
                continue

            if statement_type in requested_statements:
                print(f"You have already requested the {statement_type}. Please choose another.")
                continue

            # Generate a random financial statement
            result = generate_random_financial_statement1("Demo Company", statement_type)
            print("\nGenerated Financial Statement:\n")
            for key, value in result.items():
                print(f"{key}: {value}")
            requested_statements.add(statement_type)

        elif request.lower() == "no":
            while True:
                try:
                    ebitda_input = float(input("Enter your calculated Year 1 EBITDA (in millions): "))
                    debt_input = float(input("Enter your calculated Acquisition Debt (in millions): "))
                except ValueError:
                    print("Invalid input. Please enter numeric values.")
                    continue
                else:
                    print(f"\nYour Input Summary:\nEBITDA: ${ebitda_input}M\nAcquisition Debt: ${debt_input}M")
                    break
            break
        else:
            print("Please answer Yes or No.")

def main():
    while True:
        user_command = input("Type 'start' to generate a question: ")
        if user_command.strip().lower() == "start":
            process_input1(user_command)
            break
        else:
            print("Please type 'start' to begin.")

if __name__ == "__main__":
    main()