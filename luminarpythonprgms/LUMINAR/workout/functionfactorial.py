def fact():

    num=int(input("enter the number"))
    res=1

    for i in range(1,(num+1)):

        res=res*i

    print(res)

fact()