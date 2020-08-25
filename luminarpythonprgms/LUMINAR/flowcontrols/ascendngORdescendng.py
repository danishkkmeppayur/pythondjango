num1=int(input("enter first number"))
num2=int(input("enter second number"))
num3=int(input("enter third number"))

if((num1>num2)&(num1>num3)):
    if(num2>num3):
        print("descending order is=",num1,num2,num3)
    elif(num3>num2):
        print("descending order is=",num1,num3,num2)

elif((num2>num1)&(num2>num3)):
    if(num1>num3):
        print("descending order is=",num2,num1,num3)
    elif(num3>num1):
        print("descending order is=",num2,num3,num1)

elif((num3>num1)&(num3>num2)):
    if(num1>num2):
        print("descending order is=",num3,num1,num2)
    elif(num2>num1):
        print("descending order is=",num3,num2,num1)
