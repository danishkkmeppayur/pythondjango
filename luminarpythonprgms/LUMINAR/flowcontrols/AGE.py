bdate=int(input("enter birth date"))
bmonth=int(input("enter birth month"))
byear=int(input("enter birth year"))

cdate=int(input("enter current date"))
cmonth=int(input("enter current month "))
cyear=int(input("enter current year"))

age=cyear-byear


if(bmonth>=cmonth):
    age=age-1
elif(bmonth==cmonth):
    if(bdate>cdate):
        age=age-1

print("age is",age)
