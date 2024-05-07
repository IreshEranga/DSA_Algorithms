#b) Implement the bubblesort algorithm.
#) Read 8 numbers from the keyboard and store them in an array. Sort the numbers using 
#the bubble sort algorithm. 
A=[]   #declare array

for i in range(0,8):
    A.append(int(input("Enter a number : ")))
print(A)    

def BUBBLESORT(A):
    for i in range(1,len(A)-1):
        for j in range(1,len(A)-i+1):
            if A[j] < A[j-1]:
                A[j],A[j-1]=A[j-1],A[j]

BUBBLESORT(A)
print("Sorted Array : ",A)
