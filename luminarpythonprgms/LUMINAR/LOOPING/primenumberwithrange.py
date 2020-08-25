lowlimit=int(input("enter lower limit"))
uplimit=int(input("enter upper limit"))


for i in range(lowlimit,(uplimit+1)):
    flg=0
    for j in range(lowlimit,i):
        if(i%j==0):
            flg=1
        else:
            flag=0

    if(flg==0):
        print("prime",i)