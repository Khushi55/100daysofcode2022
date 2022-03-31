def search(list,n):
    lower=0
    upper=len(list)-1
    while lower<=upper:
       mid=(upper+lower)//2
       if list[mid]==n:
         return mid
       elif list[mid]>n:
        upper=mid - 1
       else:
        lower=mid+1
    return -1






list=[1,4,7,9,15,19,20]
n=19


res=search(list,n)
if res==-1:
    print("Element not found")
else:
    print("Element present at index:",res, list[res])
