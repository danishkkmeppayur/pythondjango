class Bank:

    def __int__(self,acno,pname,balance,bname):

        self.acno=acno
        self.pname=pname
        self.balance=3000
        self.bname="SBK"

    def deposit(self,amt):

        self.balance+=amt

        print("your",self.bname,"has been credited with",amt,"on",datatime.data.today())

    def withdraw(self,amt):
        if(amt>self.balance):
            print("transaction cancelled error code 1101")



        else:
            self.balance-=amt
            print("your",self.pname,"has been debited with",amt,"on",datatime.date.today)


    def balanceenquiry(self):

        print("your current balance=",self.balance)


obj=Bank(1001,"ajay")

obj.deposit(5000)

obj.balanceenquiry()


