# Python Bank
# TODO:
# Utilize bank funds, possibly.
# Multiple users working with the same state?


class User:
    def __init__(self, name, account, bank):
        self.name = name
        self.account = account
        self.bank = bank

    def request_balance(self):
        return self.bank.retrieve_balance(self.account)

    def request_withdraw(self, amount):
        return self.bank.attempt_withdraw(self.account, amount)

    def request_deposit(self, amount):
        return self.bank.attempt_deposit(self.account, amount)

    def request_bill_pay(self, amount, institution):
        return self.bank.attempt_bill_pay(self.account, amount, institution)


class Bank:
    def __init__(self):
        self.bankFunds = 0

    def retrieve_balance(self, account_number):
        return account_number.provide_balance()

    def attempt_withdraw(self, account_number, amount):
        if account_number.handle_withdraw(amount):
            self.bankFunds -= amount
            return f"\nHere's your ${amount}."
        else:
            return '\nInsufficient funds.'

    def attempt_deposit(self, account_number, amount):
        self.bankFunds += amount
        return f'\nThank you. Your new balance is ${account_number.handle_deposit(amount)}.'

    def attempt_bill_pay(self, account_number, amount, institution):
        if account_number.handle_withdraw(amount):
            self.bankFunds -= amount
            return f"\nWe've forwarded ${amount} to {institution} for you."
        else:
            return '\nInsufficient funds.'


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


def atmGreeting():

    action = input(
        f'\nWelcome to BKCU, {user_test.name}. How can we serve you today?\n"Check Balance"\n"Withdraw"\n"Deposit"\n"Bill Pay"\n"Exit"\n\n').lower()
    while True:
        if action == 'check balance':
            print(f'\nYour balance is ${user_test.request_balance()}.')
        elif action == 'withdraw':
            amount = input('\nSure, how much would you like to withdraw?\n$')
            print(user_test.request_withdraw(int(amount)))
        elif action == 'deposit':
            amount = input('\nWonderful, how much will you deposit?\n$')
            print(user_test.request_deposit(int(amount)))
        elif action == 'bill pay':
            institution = input(
                '\nSure, who are we sending the money to?').lower()
            amount = input('\nAnd how much would you like to send?\n$')
            print(user_test.request_bill_pay(int(amount), institution))
        elif action == 'exit':
            break
        else:
            print('Try again, please.\n')
        if action != 'exit':
            action = input(
                f'\nWhat else can I do for you, {user_test.name}?\n"Check Balance"\n"Withdraw"\n"Deposit"\n"Bill Pay"\n"Exit"\n\n').lower()

    print('\nHave a nice day. Thank you for banking with BKCU.')


bank_test = Bank()
account_test = Account('1')
user_test = User('Brian', account_test, bank_test)
atmGreeting()
