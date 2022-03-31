# linear search

def search(arr,x,n):
      for i in range(0,n):
        if arr[i]==x:
            return i

      return -1


arr=[3,5,2,8,10,20]
n=len(arr)-1
print(n)
x=6
result=search(arr,x,n)
if result==-1:
    print("Element is not present in list")
else:
    print("Element is present at Index=", result)

