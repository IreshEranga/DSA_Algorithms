#Write a program to sort a set of numbers using selection sort algorithm

#declare array
A=[]

for i in range(0,6):
    A.append(int(input("Enter a number : ")))

print(A)


def SELECTIONSORT(A):
    n=len(A)
    for j in range(0,n-1):
        smallest=j
        for i in range(j+1,n):
            if A[i] < A[smallest]:
                smallest=i
            A[j],A[smallest]=A[smallest],A[j]
            

SELECTIONSORT(A)
print("Sorting data : ", A)
            
