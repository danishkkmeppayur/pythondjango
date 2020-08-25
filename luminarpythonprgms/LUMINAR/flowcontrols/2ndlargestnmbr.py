num1=int(input("enter the number1"))
num2=int(input("enter the number2"))
num3=int(input("enter the number3"))

if((num1>num2)&(num1<num3)):
    print("num1 is second",num1)
elif((num2>num1)&(num2<num3)):
    print("num2 is second",num2)
elif((num3>num1)&(num3<num2)):
    print("num3 is second")
else:
    print("all are same")

#this program is wrong