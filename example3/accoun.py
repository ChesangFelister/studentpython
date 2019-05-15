class Bankaccount: 
    def __init__(self): 
        self.balance=0
       return("Hello!!!Welcome to you bankaccount") 
  
    def deposit(self): 
        amount=float(input("Enter amount to be Deposited: ")) 
        self.balance += amount 
        return(" Amount Deposited:",amount) 
  
    def withdraw(self): 
        amount = float(input("Enter amount to be Withdrawed: ")) 
        if self.balance>=amount: 
            self.balance-=amount 
           return(" You Withdrawed:", amount) 
        else: 
            return("sorry you have insufficient balance  ") 
  
    def display(self): 
        return("Available Balance=",self.balance) 