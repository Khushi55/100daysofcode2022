#binary search using recursion

def binary_search(arr,l,r,x):
    while l<=r:
     mid=l+(r-l) // 2
     print(mid)
     if arr[mid]==x:
        return mid

     elif arr[mid]< x:
        l= mid + 1
     else:
        r= mid - 1

    return -1

arr=[2,4,8,16,32,64]
x=16

result=binary_search(arr,0,len(arr)-1,x)
if result!=-1:
    print( "Element is present at index: ", result)
else:
    print('Element is not present in the list')

