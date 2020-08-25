lst=[1,2,3,4,5,6,7,8,9,10]

element=int(input("enter the element"))
flg=0

for i in lst:

    if(i==element):
        flg=1

        break
    else:
        flg=0

if(flg==1):

    print("found=",element)

else:
    print("not found")




