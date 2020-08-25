lst=(1,2,3,4,5)

num=int(input("enter the element"))

low=0

upp=len(lst)-1


while(low<=upp):

    data=lst[low]+lst[upp]

    if(data==num):

        print("pair=",lst[low],lst[upp])
        break

    elif(data>num):

        upp-=1

    else:

        low+=low

