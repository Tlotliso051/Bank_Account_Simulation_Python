class Account():
    """
    Represents a bank account with basic operations like deposit, withdraw, and balance inquiry.
    
    Attributes:
    - name (str): The name associated with the account.
    - balance (int): The current balance of the account.
    - password (str): The password required to perform transactions on the account.
    """

    def __init__(self, name, balance, password):
        """
        Initializes a new instance of the Account class.

        Parameters:
        - name (str): The name associated with the account.
        - balance (int): The initial balance of the account.
        - password (str): The password required to perform transactions on the account.
        """
        self.name: str = name
        self.balance: int = balance
        self.password: str = password


    def deposit(self, amountToDeposit, password):
        """
        Deposits the specified amount into the account.

        Parameters:
        - amountToDeposit (int): The amount to be deposited into the account.
        - password (str): The password required to authorize the transaction.

        Returns:
        - int or None: The new balance if the deposit is successful, None otherwise.
        """
        if password != self.password:
            print('Incorrect pin')
            return None
        elif amountToDeposit < 0:
            print('You cannot deposit a negative amount')
            return None
        self.balance += amountToDeposit
        return self.balance
    

    def withdraw(self, amountToWithdraw, password):
        """
        Withdraws the specified amount from the account.

        Parameters:
        - amountToWithdraw (int): The amount to be withdrawn from the account.
        - password (str): The password required to authorize the transaction.

        Returns:
        - int or None: The new balance if the withdrawal is successful, None otherwise.
        """
        if password != self.password:
            print('Incorrect pin')
            return None
        elif amountToWithdraw > self.balance:
            print('You cannot withdraw more than your balance, withdraw a lesser amount')
            return None
        elif amountToWithdraw <= 0:
            print('You cannot withdraw a negative or zero amount')
            return None
        self.balance -= amountToWithdraw
        return self.balance
    

    def get_balance(self, password):
        """
        Retrieves the current balance of the account.

        Parameters:
        - password (str): The password required to authorize the balance inquiry.

        Returns:
        - int or None: The current balance if the inquiry is successful, None otherwise.
        """
        if password != self.password:
            print('Incorrect pin')
            return None
        return self.balance
    

    def show(self):
        """
        Displays the account details including name, balance, and password.
        """
        print('         Name:', self.name)
        print('         Balance:', self.balance)
        print('         Password:', self.password)
        print()
