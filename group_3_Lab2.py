# define class
class Customer:
    # define constructors
    def __init__(self, name:str, account_type:str, opening_balance:float = 0.00):
        self._name = name
        self._account_type = account_type
        self._opening_balance = opening_balance
    # input validation method
    def invalid_opening_balance_error(self):
        if 50 < opening_balance < 2000000:
            self._opening_balance = opening_balance
        else:
            print("Opening balance must be between 50 and 2000000 dollars")

class Account(self):
    interest_rate = 1.05
    def set_interest_rate(self):
        pass
    def calculate_interest(self):
        interest = opening_balance * interest_rate
    def calculate_closing_balance(self):
        closing_balance = interest + opening_balance
    class StandardAccount(Account):
        pass
    class HighYieldAccount(Account):
        pass
