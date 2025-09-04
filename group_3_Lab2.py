# define class
class Customer:
    # define constructors
    def __init__(self, name:str, account_type:str, opening_balance:float = 0.00):
        self._name = name
        self._account_type = account_type
        self._opening_balance = opening_balance
    # input validation method
    def invalid_opening_balance_error(self):
        if 50 <= opening_balance <= 2000000:
            self._opening_balance = opening_balance
        else:
            print("Opening balance must be between 50 and 2000000 dollars")
    def invalid_name_error(self):
        if self._name == "":
            print("Name must not be empty")
        else:
            self._name = name

class Account:
    def __init__(self, interest_rate:float, closing_balance:float = 0.00):
        self._interest_rate = interest_rate
        self.closing_balance = closing_balance
    interest_rate = 0.05
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


num_customers = int(input("Please enter the number of customers: "))
customers = []
for customer in range(num_customers):
    customer_name = input("Please enter the customer name: ")
    if customer_name != "":
        customer_name = customer_name
    else:
        print("Customer name cannot be empty")
    customer_opening_balance = float(input("Enter opening balance: "))
    if 50 <= customer_opening_balance <= 2000000:
        customer_opening_balance = customer_opening_balance
    else:
        print("Opening balance must be between 50 and 2000000 dollars")
    if customer_opening_balance <= 50000:
        customer_account_type = "Bronze"
    if customer_opening_balance <= 100000:
        customer_account_type = "Silver"
    if customer_opening_balance <= 150000:
        customer_account_type = "Gold"
    else:
        customer_account_type = "Diamond"
    customers.append((customer_name, customer_opening_balance, customer_account_type))
print(customers)
