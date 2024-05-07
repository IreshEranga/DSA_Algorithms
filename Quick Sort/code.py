A=[]

for i in range(7):
    A.append(int(input("Enter a number : ")))
print(A)


def partition(A,low,high):
    x=A[high]
    i=low-1
    for j in range(low,high):
        if A[j] <= x:
            i=i+1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[high]=A[high],A[i+1]
    return(i+1)
def QUICKSORT(A,low,high):
    if low < high:
        q=partition(A,low,high)
        QUICKSORT(A,low,q-1)
        QUICKSORT(A,q+1,high)

QUICKSORT(A,0,len(A)-1)
print("Sorted Array : ")
for i in range(len(A)):
    print(A[i])
    
