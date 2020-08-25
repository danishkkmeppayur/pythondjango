num1=int(input("enter the number1"))
num2=int(input("enter the number2"))


try:

    res=num1/num2

    print("result=",res)

    print("executed")

except Exception as e:

    print(e.args)

finally:

    print("danish")

