"""Import the Account class from the Account.py file."""
from Account import Account

def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    cdaccount = Account(balance, interest_rate)
    monthly_intrate = cdaccount.interest / 12 /100 
    cd_updated_balance = cdaccount.balance * (1 + monthly_intrate) ** months # Update the CD account balance by adding the interest earned
    cd_interest_earned = cd_updated_balance - cdaccount.balance # Calculate interest earned
    cdaccount.set_balance(cd_updated_balance) # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    cdaccount.set_interest(cd_interest_earned) # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    
    return cd_updated_balance, cd_interest_earned # Return the updated balance and interest earned.

    # Calculate interest earned
    # ADD YOUR CODE HERE

    # Update the CD account balance by adding the interest earned
    # ADD YOUR CODE HERE

    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE

    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE

    # Return the updated balance and interest earned.
    #return  # ADD YOUR CODE HERE
