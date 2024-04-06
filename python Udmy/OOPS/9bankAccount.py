class Account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no
        
    #debit
    def debit(self, amount):
        self.balance -= amount
        print(f"Rs {amount} is debited")
        print("tota balance = ", self.get_balance())
        
    #Credit
    def Credit(self, amount):
        self.balance += amount
        print(f"Rs {amount} is credited")
        print("tota balance = ", self.get_balance())
     
    def get_balance(self):
        return self.balance 
      
acc1 = Account(10000, 173621939)
acc1.debit(1000)
acc1.Credit(500)
        