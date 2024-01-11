account_name = ''
account_balance = 0
account_password = ''

def new_account(name, balance, password):
    """
    Create a new bank account with the provided name, balance, and password.

    Parameters:
    - name (str): The name associated with the account.
    - balance (float): The initial balance of the account.
    - password (str): The password required to access the account.
    """
    global account_name, account_balance, account_password
    account_name = name
    account_balance = balance
    account_password = password


def show():
    """
    Display information about the current bank account.
    """
    global account_name, account_balance, account_password
    print(f'         Name             : {account_name}')
    print(f'         Balance          : {account_balance}')
    print(f'         Account Password : {account_password}')
    print()


def deposit(amount_to_deposit, user_password):
    """
    Deposit funds into the bank account.

    Parameters:
    - amount_to_deposit (float): The amount of money to be deposited.
    - user_password (str): The password for account verification.

    Returns:
    - float or None: The new account balance if successful, None otherwise.
    """
    global account_balance, account_password
    
    if user_password != account_password:
        print('Incorrect Password')
        return None
    elif amount_to_deposit < 0 :
        print('You cannot deposit a negative amount')
        return None
    
    account_balance += amount_to_deposit
    print(f'Your new balance is: {account_balance}')
    print()
    return account_balance

    
def get_balance(user_password):
    """
    Get the current balance of the bank account.

    Parameters:
    - user_password (str): The password for account verification.

    Returns:
    - float or None: The account balance if successful, None otherwise.
    """
    global account_balance, account_password
    if user_password != account_password:
        print('Incorrect password')
        return None
    
    return account_balance
    

def withdraw(amount_to_withdraw, user_password):
    """
    Withdraw funds from the bank account.

    Parameters:
    - amount_to_withdraw (float): The amount of money to be withdrawn.
    - user_password (str): The password for account verification.

    Returns:
    - float or None: The new account balance if successful, None otherwise.
    """
    global account_balance, account_password

    if user_password != account_password:
        print('Incorrect Password')
        return None
    elif amount_to_withdraw < 0:
        print('You cannot withdraw a negative amount')
        return None
    elif amount_to_withdraw > account_balance:
        print('Amount requested is greater than amount available')
        return None
    
    account_balance -= amount_to_withdraw
    print(f'Your new balance is: {account_balance}')


while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawal')
    print('Press s to show the account')
    print('Press q to quit')
    print()

    action = input('What do you want to do? ').lower()
    action = action[0]
    print()

    if action == 'b':
        print('Get Balance')
        user_password = input('Enter the password: ')
        the_balance = get_balance(user_password)
        if the_balance is not None:
            print(f'Your balance is: {account_balance}')
        
    elif action == 'd':
        print('Deposit')
        print()
        user_password = input('Enter the password: ')
        deposit_amount = input('Please enter the amount to deposit: ')
        try:
            deposit_amount = float(deposit_amount)
        except ValueError:
            print("Please use only numbers.")
        new_balance = deposit(deposit_amount, user_password)
        if new_balance is not None:
            show()
            print(f'Your new balance is: {account_balance}')

    new_account('tlotliso', 100, 'arthur')
