#a) Write a program to read a set of numbers (between 10  to 20) from the keyboard and store 
#them in an array.

#insertion sort algorithm
#declare an array / creating an empty list
A=[]

#number of elements as input
n=9

for i in range(0,n):
    number = int(input("Enter a number: "))
    if(number>10 and number<20):
        A.append(number)
    else:
        print("Invalid Number ...")
    i=i+1

print(A)

#b) Sort the numbers in ascending order with the Insertion sorting algorithm. 

#declaring new method
def INSERTIONSORT(A):
    for j in range (2,len(A)): #traverse the length of the array
        key = A[j]
        i=j-1
        while i>=0 and A[i]>key:
            A[i+1]=A[i]
            i=i-1
        A[i+1]=key

INSERTIONSORT(A)
print("Sorted Array ",A)
            
        
