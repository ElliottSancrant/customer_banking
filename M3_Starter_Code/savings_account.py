"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account
# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """

    account = Account(balance, interest_rate) # Create an instance of the `Account` class and pass in the balance and interest parameters.
    monthly_intrate = account.interest / 12 /100 
    savings_updated_balance = account.balance * (1 + monthly_intrate) ** months # Calculate interest earned
    savings_interest_earned = savings_updated_balance - account.balance # Update the savings account balance by adding the interest earned
    account.set_balance(savings_updated_balance) # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    account.set_interest(savings_interest_earned) # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    
    return savings_updated_balance, savings_interest_earned # Return the updated balance and interest earned.




    

    
    


    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE

    # Calculate interest earned
     # ADD YOUR CODE HERE

    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE

    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE

    # Return the updated balance and interest earned.
   # return  # ADD YOUR CODE HERE
