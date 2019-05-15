class Account:
    def __init__(self,first_name,second_name):
        self.first_name=first_name
        self.second_name=second_name
        self.balance=0.00
        self.deposit=[]
        self.withdraw=[]
	
	def greetings(self):
            return"Hello {} {} welcome to the your banking account you balance is{}".format(self.first_name,self.second_name,self.balance)

    def deposit(self,d):
        self.balance=self.balance+d
        self.deposit.append(d)
        return("you have deposited {}".format(d))

    def show_deposit(self):
		for d in self.deposit: 
		print (d)
		    

    def withdraw(self,amountsh):
        if amountsh < self.balance:
            self.balance=self.balance-amountsh
       
            return("Hello {} {} you have successfully withdrawn  {}".format(self.first_name,self.second_name,amountsh))
        else:
            return("Hello {} {} you have insufficient balance".format(self.first_name,self.second_name,amountsh))
    def showbalance(self):
        balance=self.balance
        return("Hello {} {} your balance is {}".format(self.first_name,self.second_name))
            
        