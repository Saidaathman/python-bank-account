class BankAccount:
   

    def _init_(self, first_name, last_name, phone_no, bank):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_no = phone_no
        self.bank = bank
        self.balance = 0
        self.withdraw_statement = []
        self.deposit_statement = []
        self.loan_balance = 0

    def account_name(self):
        name = "{} account for {} {}".format(
            self.bank, self.first_name, self.last_name, self.phone_no, self.bank)
        return name

    def deposit(self, amount):

   
      if amount <= 0:
               
          print("You cannot deposit zero or negative")
      else:
            self.balance += amount
            print("You have deposited {} to {}".format(amount, self.account_name()))
            return 
            
            
          
    def withdraw(self, amount):
         
      if amount <= 0:
          print("You cannot withdraw zero or negative")
          
       
      elif amount > self.balance:
            print("You don't have enough balance")
      else:
            self.balance -= amount
            print("You have withdrawn {} from {}".format(amount, self.account_name()))


    def get_balance(self):
   
        return "The balance for {} is {}".format(self.account_name(), self.balance)
         
     def give_loan(self, loan):
      if loan <= 0:
        print("Too low")
        
      else: 
        self.loan_balance += loan
        print("{} you have borrowed {}".format(self.account_name(), loan))
      
    def pay_loan(self, loan):
      if loan <= 0:
        print("Too low")
      else:
        self.loan_balance -= loan
        print(" You have repaid {}".format(loan))



//from datetime import datetime
time = datetime.now()
print(time)
class BankAccount:
    def _init_(self, first_name, last_name, Phone_no, bank):
        self.first_name = first_name
        self.last_name = last_name
        self.Phone_no = Phone_no
        self.bank = bank
        self.withdrawals = []
        self.deposits =[]
        self.balance = 0
        self.loan = 0

    def account_name(self):
        name = "{}  account for {} {}".format(self.bank, self.first_name, self.last_name)
        return name

    def deposit(self, amount):
        try:
            amount + 1
        except TypeError:
            print("You must enter the amount in figures")
            return

        if amount <= 0:
            print("You cannot deposit zero or negative")
         
        else:
            self.balance += amount
            self.deposits.append(amount)
            formated_time = time.strftime("%A, %drd %B %Y, %H:%M %p")
            print("You have deposited {} to {} on {}".format(amount, self.account_name(), formated_time))
            return
    def withdraw(self, amount):
        try:
            amoount + 1
        except TypeError:
            print("You must enter the amount in figures")
            return

        if amount <= 0:
            print("You cannot deposit zero or negative")

        elif amount > self.balance:
            print("You have insufficient funds to withdraw this amount")
        
        else:
            self.balance -= amount
            self.withdrawals.append(amount)
            print("You have withdrawn {} from {}".format(amount, self.account_name()))

    def get_balance(self):
     return "The balance for {} is {}".format(self.account_name(), self.balance)

    def show_deposit_statements(self):
        for deposit in self.deposits:
            formated_time = time.strftime("%A, %drd %B %Y, %H:%M %p")
            print("{} deposited on {}".format(deposit, formated_time))
 
    def show_withdrawals_statement(self):
        for withdraw in  self.withdrawals:
            print(withdraw)

    def request_loan(self, amount):
        try:
            amount + 1
        except TypeError:
            print("You must enter the amount in figures")
            return

        if amount <= 0:
            print("You cannot request for an amount low than zero")
        else:
             self.loan = amount
             print("You have been given a loan of {}".format(amount))

    def repay_loan(self, amount):
        try:
            amount + 1
        except TypeError:
            print("You must enter the amount in figures")
            return

        if amount <= 0:
            print("Too low t repa your amount")
        elif self.loan == 0:
            print("You don't have a loan at the moment")
        elif amount > self.loan:
            print("Your loan is {} please enter an amount that is less or equal".format(self.loan))
        else:
            self.loan -= amount
            print("You have repaid you loan with {} your balance is {}".format(amount, self.loan))


acc1 = BankAccount("mariam", "said", +25487622638, "KCB")
acc1.first_name
acc1.deposit(100)
print(acc1.first_name)
acc1.deposit(5632)
print(acc1.balance)
acc1.request_loan(2000)
acc1.repay_loan(1000)
acc1.repay_loan(56988)
acc1.repay_loan(1000)
print(acc1.loan)
print(acc1.balance)
acc1.request_loan(458999)
acc1.deposit(400)
acc1.deposit("ten")
acc1.deposit(8050)
acc1.deposit(9369)
acc1.show_deposit_statements()
acc1.request_loan("twenty")

//
from datetime import datetime
time = datetime.now()
print(time)

class Account:
    def _init_(self, first_name, last_name, Phone_no):
        self.first_name = first_name
        self.last_name = last_name
        self.Phone_no = Phone_no
        self.withdrawals = []
        self.deposits =[]
        self.balance = 0
        self.loan = 0
        self.loan_repayments = []

class BankAccount(Account):
    def _init_(self, first_name, last_name, phone_number, bank):
        self.bank = bank
        super()._init_(first_name, last_name, phone_number)

class MobileMoneyAccount(Account):
    def _init_(self, first_name, last_name, phone_number, service_provider):
        self.service_provider = service_provider
        super()._init_(self, first_name, last_name, phone_number)
       
        

    def account_name(self):
        name = "  account for {} {}".format(self.first_name, self.last_name)
        return name

    def deposit(self, amount):
        try:
            amount + 1
        except TypeError:
            print("You must enter the amount in figures")
            return

        if amount <= 0:
            print("You cannot deposit zero or negative")
         
        else:
            self.balance += amount
            time = datetime.now()
            deposit = {
                "time": time,
                "amount": amount
            }
            self.deposits.append(deposit)
            formatted_time = time.strftime("%A, %drd %B %Y, %H:%M %p")
            print("You have deposited {} to {} on {}".format(amount, self.account_name(), formatted_time))
            
    def withdraw(self, amount):
        try:
            amount + 1
        except TypeError:
            print("You must enter the amount in figures")
            return

        if amount <= 0:
            print("You cannot deposit zero or negative")

        elif amount > self.balance:
            print("You have insufficient funds to withdraw this amount")
        
        else:
            self.balance -= amount
            self.withdrawals.append(amount)
            print("You have withdrawn {} from {}".format(amount, self.account_name()))

    def get_balance(self):
     return "The balance for {} is {}".format(self.account_name(), self.balance)

    def get_formatted_time(self, time):
        return time.strftime("%A, %drd %B %Y, %H:%M %p")

    def show_deposit_statements(self):
        for deposit in self.deposits:
            formated_time = time.strftime("%A, %drd %B %Y, %H:%M %p")
            print("{} deposited on {}".format(deposit, formated_time))
 
    def show_withdrawals_statement(self):
        for withdraw in  self.withdrawals:
            time = withdraw["time"]
            formated_time = self.get_formatted_time(time)
            amount = withdrawal["amount"]
            statement = "You withdrew {} on {}".format(amount, formated_time)
            print(withdraw)

    def request_loan(self, amount):
        try:
            amount + 1
        except TypeError:
            print("You must enter the amount in figures")
            return

        if amount <= 0:
            print("You cannot request for an amount low than zero")
        else:
             self.loan = amount
             print("You have been given a loan of {}".format(amount))

    def repay_loan(self, amount):
        try:
            amount + 1
        except TypeError:
            print("You must enter the amount in figures")
            return

        if amount <= 0:
            print("Too low t repa your amount")
        elif self.loan == 0:
            print("You don't have a loan at the moment")
        elif amount > self.loan:
            print("Your loan is {} please enter an amount that is less or equal".format(self.loan))
        else:
            self.loan -= amount
            time = datetime.now()
            repayment = {
                "time": time,
                "amount": amount
            }
            self.loan_repayments.append(repayment)
            print("You have repaid you loan with {} your balance is {}".format(amount, self.loan))
    
    def loan_repayment_statement(self):
        for repayment in self.loan_repayments:
            time = repayment["time"]
            amount = repayment["amount"]
            formatted_time = self.get_formatted_time(time)
            statement = "You repaid {} on {} ".format(amount, formatted_time)
            print(statement)


    class BankAccount(Account):
        def _init_(self,first_name,last_name,phone_number,bank):
            self.bank=bank
            super()._init_(first_name,last_name,phone_number)


    class MobileMoneyAccount(Account):
        def _init_(self,first_name,last_name,phone_number,service_provider):
            self.service_provider=service_provider
            self.airtime=[]
            super()._init_(first_name,last_name,phone_number)

        def buy_airtime(self,amount):
            try:
               amount + 1
            except TypeError:
             print("You must enter the amount in figures")
             return 
        if amount >self.balance:
            print("You don't have enoough balance,your balance is {}".format(self.balance))
        else:
            self.balance-=amount
            time=datetime.now()
            airtime={
                'time':time,
                "airtime":amount
            }
            self.airtime.append(airtime)
            print("You have bought airtime worth {} on {}".format(amount,formatted_time(time)))

        def pay_bill(self,amount):
            try:
               amount + 1
            except TypeError:
             print("You must enter the amount in figures")
             return 
        if amount > self.balance:
            print("Sorry you don't have enough money to pay the bills,your balance is {}".format(self.balance))
        else:
            self.balance-=amount
            time=datetime.now()
            bills={
                'time':time,
                'bills':amount
            }
            self.bills.append(bills)
            print("You paid your bills worth {} on {}".format(amount,formatted_time(time)))

        def send_money(self,amount):
            try:
                amount + 1
            except TypeError:
             print("You must enter the amount in figures")
             return 
             if amount >self.balance:
                 print("Sorry you dont have enough money to do the transaction,your current balance is {}".format(self.balance))
             else:
                 self.balance-=amount
                 time=date.now()
                 money={
                     'time':time,
                     'money':amount
                 }
            self.money.append(money)
            print("You sent {} on {}".format(amount,formatted_time(time)))

        def receive_money(self,amount):
            print("You received {} on {},your balance is {}".format(amount,formatted_time(time),self.balance))

    
        