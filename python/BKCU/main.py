# Python Bank
# TODO: 


class User:
    def __init__(self, name, account, bank):
        self.name = name
        self.account = account
        self.bank = bank

    def request_balance(self):
        return self.bank.retrieve_balance(self.account)

    def request_withdraw(self, amount):
        return self.bank.retrieve_balance(self.account, amount)

    def request_deposit(self, amount):
        return self.bank.attempt_deposit(self.account, amount)

    def request_bill_pay(self, amount, institution):
        return self.bank.attempt_bill_pay(self.account, amount, institution)


class Bank:
    def __init__(self):
        self.bankFunds = 0

    def retrieve_balance(self, account_number, amount=None):
        if amount == None:
            return account_number.provide_balance()
        else:
            if account_number.handle_withdraw(amount):
                self.bankFunds -= amount
                return f"Here's your ${amount}."
            else:
                return 'Insufficient funds.'

    def attempt_deposit(self, account_number, amount):
        self.bankFunds += amount
        return f'Thank you. Your new balance is ${account_number.handle_deposit(amount)}.'

    def attempt_bill_pay(self, account_number, amount, institution):
        if account_number.handle_withdraw(amount):
            self.bankFunds -= amount
            return f"We've forwarded ${amount} to {institution} for you."
        else:
            return 'Insufficient funds.'


class Account():

    def __init__(self, id):
        self.id = id
        self.balance = 0

    def provide_balance(self):
        return self.balance

    def handle_withdraw(self, amount):
        if amount > self.balance:
            return False
        else:
            self.balance -= amount
            return True

    def handle_deposit(self, amount):
        self.balance += amount
        return self.balance

    def handle_bill_payment(self, amount, institution):
        if amount > self.balance:
            return False
        else:
            self.balance -= amount
            return True


bank_test = Bank()
account_test = Account('1')
user_test = User('Brian', account_test, bank_test)
user_test.request_deposit(40)
print(user_test.request_bill_pay(20, 'test company'))

# The user needs to be able to look up their balance
# The program needs to keep running until the user decides to quit the program.
