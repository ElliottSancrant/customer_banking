# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account
# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    print("For the Savings Account")
    while True:
        interest_rateinput = input("Enter the current APR interest rate (For example, 15 for 15%): ")
        try:
            savings_interest = float(interest_rateinput)
            if savings_interest > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("You must enter a valid number.")


    while True:
        balanceinput = input("How much would you like to deposit into the savings account?: ")
        try:
            savings_balance = float(balanceinput)
            if savings_balance > 0:
                break
            else:
                print("Please enter a positive amount.")
        except ValueError:
            print("You must enter a valid number.")
    while True:
        monthsinput = input("How many months will the money be in the savings account?: ")
        try:
            savings_maturity = int(monthsinput)
            if savings_maturity >= 0:
                break
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("You must enter a valid number.")
    # Call the create_savings_account function and pass the variables from the user.
    savings_updated_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Savings balance: {savings_updated_balance:.2f} \nInterest earned:  {savings_interest_earned:.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    print("For the CD account")
    while True:
        cdinterest_rateinput = input("Enter the current APR interest rate (For example, 15 for 15%): ")
        try:
            cd_interest = float(cdinterest_rateinput)
            if cd_interest > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("You must enter a valid number.")


    while True:
        cdbalanceinput = input("How much would you like to deposit into the CD account?: ")
        try:
            cd_balance = float(cdbalanceinput)
            if cd_balance > 0:
                break
            else:
                print("Please enter a positive amount.")
        except ValueError:
            print("You must enter a valid number.")
    while True:
        cdmonthsinput = input("How many months will the money be in the CD account?: ")
        try:
            cd_maturity = int(cdmonthsinput)
            if cd_maturity >= 0:
                break
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("You must enter a valid number.")


    # Call the create_cd_account function and pass the variables from the user.
    cd_updated_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"CD balance: {cd_updated_balance:.2f}, \nInterest earned: {cd_interest_earned:.2f}")

if __name__ == "__main__":
    # Call the main function.
    main()