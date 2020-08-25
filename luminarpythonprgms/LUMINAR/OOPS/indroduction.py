class employee:
    def __init__(self,eid,ename,desig):

        self.eid=eid
        self.ename=ename
        self.desig=desig

    def printvalues(self):

        print(self.eid)
        print(self.ename)
        print(self.desig)



obj=employee(1004,"dan","ceo")

print(obj.ename)

obj.printvalues()