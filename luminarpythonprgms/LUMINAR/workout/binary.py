lst=(2,3,4,5,6,7,8,9)

lst.sort()
num=int(input("enter the element"))

low=0

upp=len(lst)-1


for(low<=upp):
    mid=(low+upp)//2
    if(num<lst[mid]):

        upp=mid-1

    elif(num>lst[mid]):

        low=mid+1
