lst=[1,2,3,4]

element=int(input("enter the number"))

lst.sort()

low=0
upp=len(lst)-1

while(low<=upp):

    data=lst[low]+lst[upp]

    if(data==element):

        print(lst[low],",",lst[upp])
        break

    elif(data>element):

        upp=upp-1

    elif(data<element):

        low=low+1

