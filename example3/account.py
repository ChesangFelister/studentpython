from datetime import datetime
class Account:
    def __init__(self,first_name,second_name,):
        self.first_name=first_name
        self.second_name=second_name
        self.balance=0.00
        self.loan=0.00  
        self.total=0
        self.deposits=[]
        self.withdrawals=[]
        self.loans=[]
        
    def greetings(self):
            return"Hello {} {} welcome to the your banking account you balance is{}".format(self.first_name,self.second_name,self.balance)

    def deposit(self,amount):
        self.balance=self.balance+amount
        time=datetime.now()
        object={"time":time,"amount":amount}
        self.deposits.append(object)

        return("you have deposited {}".format(amount))

    def show_deposits(self):
        for amount in self.deposits: 
            time=amount["time"]
            formated_time=time.strftime("%c")
            amount=amount["amount"]
            print ("on {} you deposited {} ".format(formated_time,amount))
            

    def withdraw(self,amountsh):
        if amountsh < self.balance:
            time=datetime.now()
            object={"time":time,"amountsh":amountsh}
            self.withdrawals.append(object)
            self.balance=self.balance-amountsh
       
            return("Hello {} {} you have successfully withdrawn  {} at {}".format(self.first_name,self.second_name,amountsh,time))
        else:
            return("Hello {} {} you have insufficient balance".format(self.first_name,self.second_name,amountsh))
    def show_withdrawals(self):
        for amountsh in self.withdrawals:
            time=amountsh["time"]
            formated_time=time.strftime("%c")
            amountsh=amountsh["amountsh"]
            print("hello you have  withdrawn on {} {}".format(formated_time,amountsh))

    def showbalance(self):
        balance=self.balance
        return("Hello {} {} your balance is {} ".format(self.first_name,self.second_name,self.balance))

    def give_loan(self,loan):
         loan = loan
         total = 0
         for amount in self.deposits:
            amount = amount["amount"]
            total+=amount
            # time=datetime.now()#
            # object={"time":time,"loan":loan}#

         if len(self.deposits)>=5:
            loans<(total/3 )
            self.loan==0
            self.loan = self.loan + loan
            print("Dear customer your loan of {}at {} has been approved".format(loan,time))



   
    def repay_loan(self,amount):
        
        payment = amount

        self.loan.extend(amount)

        self.loan = self.loan-amount
        excess_payment = self.deposit.append(deposit)

        print( "Dear customer you have paid KES {} your remaining loan balance is now {}".format(amount,self.loan))
     









    
  #      now = datetime.datetime.now()

       # if amount < 5:
         #   print("You must enter an amount more than"{} "to repay the loan".format(self.first_name,self.second_name,amount));

        #elif not self.loan:

            #self.balance += amount
            #info = {
               # "date": time,
               # "amount": amount
            #}
            #self.deposits.append(info)
            #print("Dear,", self.name, "You have no  remain loan balance so"{}
                #  "has been deposited to your account on", time, "Your new balance is", self.balance)

        #elif amount > self.loan:
            #diff = amount - self.loan
            #old_loan = self.loan
           # self.loan = 0
            #self.balance += diff
            #info = {
               # "date": time,
                #"amount": diff
          #  }