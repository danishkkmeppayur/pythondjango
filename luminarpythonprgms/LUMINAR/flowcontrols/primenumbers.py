low=int(input("enter lower limit"))

upp=int(input("enter upper limit"))


for i in range(low,(upp+1)):

    flg=0
    for j in range(2,i):

        if(i%j==0):

            flg+=1

            break
        else:
            flg=0

    if(flg==0):
        print(i)

