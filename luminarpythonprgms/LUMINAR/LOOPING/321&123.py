num=int(input("enter the numbr"))
res=0
rev=0
while(num!=0):
    digit=num%10
    res=(res*10)+digit

    num=num//10

print(res)


