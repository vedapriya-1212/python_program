class BankAccount:
    def __init__(self,balance=0):
        self.__balance=balance

    def deposit(self,amount):
        self.__balance=self.__balance+amount 
        return self.__balance
    
    def withdraw(self,amount):
        if self.__balance>=amount:
            self.__balance=self.__balance-amount
            return self.__balance
        else:
            print("no sufficient money")

    def get_balance(self):
        print("final balance:",self.__balance)
ob=BankAccount()
ob.deposit(5000)
ob.withdraw(2000)
ob.get_balance()