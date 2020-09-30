#Created by Shelley Ophir
#Coding Dojo Sep. 30, 2020
#Understand how to chain methods
# Update your previous assignment so that each instance's methods are chained

#create class User
class User:
    #define attritbutes
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    #define methods
    def make_deposits(self, amount):
        self.account_balance += amount
        return self
    
    # make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self

    # display_user_balance(self) - have this method print the user's name and account balance to the terminal
    # eg. "User: Guido van Rossum, Balance: $150
    def display_user_balance(self):
        print("User:", self.name, "\nBalance:", self.account_balance)

    # BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.make_deposits(amount)
        return self

# Create 3 instances of the User class
birder1 = User("Brad", "email1@cardinal.com")
birder2 = User("Stu", "stu@priessler.com")
birder3 = User("Kenny", "722@bostick.com")

# Have the first user make 3 deposits and 1 withdrawal and then display their balance
birder1.make_deposits(722).make_deposits(10).make_deposits(5).make_withdrawl(15).display_user_balance()

# Have the second user make 2 deposits and 2 withdrawals and then display their balance
birder2.make_deposits(100).make_deposits(500).make_withdrawl(10).make_withdrawl(20).display_user_balance()

# Have the third user make 1 deposits and 3 withdrawals and then display their balance
birder3.make_deposits(815).make_withdrawl(10).make_withdrawl(20).make_withdrawl(30).display_user_balance()

# BONUS: have the first user transfer money to the third user and then print both users' balances
birder1.transfer_money(birder3, 100).display_user_balance()
birder3.display_user_balance()