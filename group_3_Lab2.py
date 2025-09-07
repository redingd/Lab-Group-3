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
    def toString():
        print(self._name, "\t", self._opening_balance, "\t", self._account_type) # how do you want to get interest, closing balance and account kind?

class Account:
    def __init__(self, interest_rate:float, closing_balance:float = 0.00):
        self._interest_rate = interest_rate
        self.closing_balance = closing_balance
    def set_interest_rate(self):
        interest_rate = int(input("Set interest rate to: ")) # 12.5%
    def calculate_interest(self):
        interest = opening_balance * interest_rate
    def calculate_closing_balance(self):
        closing_balance = interest + opening_balance

# define StandardAccount, which is a subclass of Account
# all methods and variables are kept the same and will call their definitions in Account
class StandardAccount(Account):
    def __init__(self, interest_rate:float, closing_balance:float = 0.00):
        super().__init__(interest_rate, closing_balance)
    def set_interest_rate(self):
        super().set_interest_rate()
    def calculate_interest(self):
        super().calculate_interest()
    def calculate_closing_balance(self):
        super().calculate_closing_balance()

# define HighYieldAccount, which is a subclass of Account
# overrides the calculate_interest method from Account, identical to StandardAccount otherwise
class HighYieldAccount(Account):
    def __init__(self, interest_rate:float, closing_balance:float = 0.00):
        super().__init__(interest_rate, closing_balance)
    def set_interest_rate(self):
        super().set_interest_rate()
    def calculate_interest(self):
        interest = opening_balance * interest_rate * (1 + (opening_balance / 100000))
    def calculate_closing_balance(self):
        super().calculate_closing_balance()

# get num of customers
num_customers = int(input("Please enter the number of customers: "))

# following values, as well as num_customers, to be used for summary statistics later on
num_bronze = 0
num_silver = 0
num_gold = 0
num_diamond = 0
num_standard = 0
num_high_yield = 0
total_interest_paid = 0.00
hightest_closing_amt = 0.00
highest_closing_name = ""
lowest_closing_amt = 0.00
lowest_closing_name = ""

customers = Customer[]

# storing customer information
for customer in range(num_customers):
    customer_name = input("Please enter the customer name: ")
    if customer_name != "":
        customer_name = customer_name
    else:
        print("Customer name cannot be empty")
    # input validation
    customer_opening_balance = float(input("Enter opening balance: "))
    if 50 <= customer_opening_balance <= 2000000:
        customer_opening_balance = customer_opening_balance
    else:
        print("Opening balance must be between 50 and 2000000 dollars")
    # Assigning account type
    if customer_opening_balance <= 50000:
        customer_account_type = "Bronze"
        num_bronze ++
    if customer_opening_balance <= 100000:
        customer_account_type = "Silver"
        num_silver ++
    if customer_opening_balance <= 150000:
        customer_account_type = "Gold"
        num_gold ++
    else:
        customer_account_type = "Diamond"
        num_diamond ++
    customers.append(Customer(customer_name, customer_opening_balance, customer_account_type))

# Print Customer Report
print("CUSTOMER REPORT \n------------------------------------------------------------------------------------")
print("Name \tOpeningBalance \tInterest Earned \tClosing Balance \tType \tAccount")
for i in range(len(customers):
    customers[i].toString()
print("Total Customers: ", num_customers)
print("By Customer Type: Bronze = ", num_bronze, ", Silver = ", num_silver, ", Gold = ", num_gold, ", Diamond = ", num_diamond)
print("By Account Kind: Standard = ", num_standard, ", High Yield = ", num_high_yield)

