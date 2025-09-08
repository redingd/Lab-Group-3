# McKinley defined classes and constructors, added account types, added highest/lowest closing account stats, and defined some methods.
# David added account kinds, formatted the output of the table, added the option to change the interest rate, some summary stats, defined some methods, and helped clarify input validation. 
# define class
class Account:
    interest_rate = 1.125
    interest = customer_opening_balance * Account.interest_rate - customer_opening_balance
    closing_balance = 0.00
    def __init__(self, interest_rate:float = 1.125, closing_balance:float = 0.00):
        self._interest_rate = interest_rate
        self.closing_balance = closing_balance
    def set_interest_rate(self, interest_rate:float):
        interest_rate = 1.125
    def calculate_interest(self):
        interest = customer_opening_balance * Account.interest_rate
        return interest
    def calculate_closing_balance(self):
        closing_balance = Account.interest + customer_opening_balance
        return closing_balance

class Customer:
    # define constructors
    def __init__(self, name:str, account_type:str, acct_kind:Account, opening_balance:float = 0.00,):
        self._name = name
        self._account_type = account_type
        self._opening_balance = opening_balance
        self._acct_kind = acct_kind
    # input validation method
    def invalid_opening_balance_error(self):
        if 50 <= customer_opening_balance <= 2000000:
            self._opening_balance = customer_opening_balance
        else:
            print("Opening balance must be between 50 and 2000000 dollars")
    def invalid_name_error(self):
        if self._name == "":
            print("Name must not be empty")
        else:
            self._name = name
    def toString():
        print(self._name, "\t", self._opening_balance, "\t", self._account_type) # how do you want to get interest, closing balance and account kind?



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
        interest = customer_opening_balance * Account.interest_rate * (1 + (customer_opening_balance / 100000))
    def calculate_closing_balance(self):
        super().calculate_closing_balance()

# ask user if they want to change interest rate
interestRate = 1.125 # defaults to 12.5%
while True: # to ensure a valid input
    ans = input("Would you like to override the default interest rate of 12.5%? Y or N: ")
    if ans == "Y":
        try:
            interestRate = float(input("Enter new interest rate: "))
            break
        except TypeError:
            print("Invalid input type, try again.")
    elif ans != "N":
        print("Not a valid input, try again.")
    else:
      break

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
# lists to be used for customer report 
customers = []
list_customer_names = []
list_opening_balances = []
list_interest_earned = []
list_closing_balances = []
list_account_type = []
list_account_kind = []

# storing customer information
for customer in range(num_customers):
    while True: # to ensure a valid input
        customer_name = input("Please enter the customer name: ")
        if customer_name != "":
          list_customer_names.append(customer_name)
          break
        else:
            print("Customer name cannot be empty, try again.")
    
    # input validation
    while True: # to ensure a valid input
        try:
            customer_opening_balance = float(input("Enter opening balance: "))
            if 50 <= customer_opening_balance <= 2000000:
                customer_opening_balance = customer_opening_balance
                list_opening_balances.append(customer_opening_balance)
                Account.calculate_interest(customer_opening_balance)
                Account.calculate_closing_balance(Account.interest)
                break
            else:
                print("Opening balance must be between 50 and 2000000 dollars, try again.")
        except TypeError:
            print("Invalid input type, try again.")

    # Assigning account type
    if customer_opening_balance <= 50000:
        customer_account_type = "Bronze"
        num_bronze += 1
        list_account_type.append(customer_account_type)
    elif customer_opening_balance <= 100000:
        customer_account_type = "Silver"
        num_silver += 1
        list_account_type.append(customer_account_type)
    elif customer_opening_balance <= 150000:
        customer_account_type = "Gold"
        num_gold += 1
        list_account_type.append(customer_account_type)
    else:
        customer_account_type = "Diamond"
        num_diamond += 1
        list_account_type.append(customer_account_type)
    # get account kind
    while True: # to ensure a valid input
        kind = input("Would you like a Standard or High Yield Account? S for Standard, H for High Yield: ")
        if kind == "S":
            acct_kind = StandardAccount(interestRate, 0.00)
            num_standard += 1
            list_account_kind.append("StandardAccount")
            # calculate interest
            Account.interest = customer_opening_balance * Account.interest_rate - customer_opening_balance
            total_interest_paid += Account.interest
            list_interest_earned.append(Account.interest)

            # calculate closing balance
            Account.closing_balance = customer_opening_balance + Account.interest
            list_closing_balances.append(Account.closing_balance)

            break
        elif kind == "H":
            acct_kind = HighYieldAccount(interestRate, 0.00)
            num_high_yield += 1
            list_account_kind.append("HighYieldAccount")
            # calculate interest
            Account.interest = customer_opening_balance * Account.interest_rate * (1 + (customer_opening_balance / 100000))
            total_interest_paid += Account.interest
            list_interest_earned.append(Account.interest)

            # calculate closing balance
            Account.closing_balance = customer_opening_balance + Account.interest
            list_closing_balances.append(Account.closing_balance)
            break
        else:
            print("not a valid input, try again.")

        
# assigning highest/lowest closing amounts
highest_closing_amt = max(list_closing_balances)
index_highest_closing_amt = list_closing_balances.index(highest_closing_amt)
highest_closing_name = list_customer_names[index_highest_closing_amt]
lowest_closing_amt = min(list_closing_balances)
index_lowest_closing_amt = list_closing_balances.index(lowest_closing_amt)
lowest_closing_name = list_customer_names[index_lowest_closing_amt]
# Print Customer Report
print("CUSTOMER REPORT \n----------------------------------------------------------------------------------------------")
print("Name \tOpeningBalance \tInterest Earned \tClosing Balance \tType \tAccount")
for customer in range(num_customers):
  print(f"{list_customer_names[customer]} \t{list_opening_balances[customer]} \t{list_interest_earned[customer]} \t{list_closing_balances[customer]} \t{list_account_type[customer]} \t{list_account_kind[customer]}")
print("----------------------------------------------------------------------------------------------")
print("Total Customers: ", num_customers)
print("By Customer Type: Bronze = ", num_bronze, ", Silver = ", num_silver, ", Gold = ", num_gold, ", Diamond = ", num_diamond)
print("By Account Kind: Standard = ", num_standard, ", High Yield = ", num_high_yield)
print("Total Interest Paid: $", total_interest_paid)
print("Highest Closing Balance: $", highest_closing_amt, " (", highest_closing_name, ")")
print("Lowest Closing Balance: $", lowest_closing_amt, " (", lowest_closing_name, ")")
