#Binary search algorithm
A=[]
for v in range(4):
    A.append(int(input("Enter a number : ")))
print(A)

x=int(input("Enter a search value : "))

def BINARYSEARCH(A,min,max,x):
    if max<min:
        return -1
    else:
        mid=(min+max)//2
        if A[mid]>x:
            return BINARYSEARCH(A,min,mid-1,x)
        elif A[mid]<x:
            return BINARYSEARCH(A,mid+1,max,x)
        else:
            return mid

#function call
result=BINARYSEARCH(A,0,(len(A)-1),x)

if result != -1:
    print("Element is present at index",str(result))
else:
    print("Element is not in the array")
            
