'''Question 17: Write a Java program to count the number of even and odd elements present in a given integer array.
Asked In Practice assignment
Input :- Array = { 10, 15, 20, 25, 30 }
Output :- Even count = 3
Odd count = 2 Explanation
? An even number is a number that is completely divisible by 2.
? An odd number is a number that is not divisible by 2.
? Traverse the array using a loop.'''


arr=[10,15,20,25,30]
ecount=0
ocount=0
for i in range(0,len(arr)):
    if arr[i]%2==0:
        ecount+=1
    else:
        ocount+=1
    
    
print("Even Count",ecount)
print("odd Count",ocount)

        
