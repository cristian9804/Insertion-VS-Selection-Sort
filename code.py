import time
import random

def sortTimeUsing(sortf,A):
    sortf(A)
    
    
    
def insertionSort(A):
    if len(A)>0:
        t = time.time()
        for i in range(1,len(A)):
            insert(A[i],A,i)
        t = time.time()-t
        print(t)
    else:
        print("Array is already sorted ")

def insert(k, A, hi):
     for i in range (hi,0,-1):
         if k >= A[i-1]:
             A[i] = k
             return
         A[i] = A[i-1]
     A[0] = k

def selectionSort(A):
    t = time.time()
    for i in range(len(A)):
        imin = findMin(i,A)
        swap(i,imin,A)
    t = time.time()-t
    print(t)
            
def findMin(i, A):
 imin = i
 for j in range(i+1,len(A)):
     if A[j] < A[imin]:
         imin = j
 return imin

def swap(i, j, A):
 tmp = A[i]
 A[i] = A[j]
 A[j] = tmp


myArray=[0 for i in range(10)] 
for i in range (len(myArray)-1):
    myArray[i] =  random.randint(0,9999)
print(myArray)

sortTimeUsing(insertionSort,myArray)
sortTimeUsing(selectionSort,myArray)

