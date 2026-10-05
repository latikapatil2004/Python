'''uestion 26: Write a java program to count all pairs of elements in an array whose sum is equal to a given number.
Asked In Practice assignment
Input:
Array = [1, 5, 7, -1, 5]
Sum = 6

Output:
Number of Pairs = 3

Explanation:
Check all possible pairs in the array and count those pairs whose sum equals the given value.'''

arr=[1, 5, 7, -1, 5]
sum=6
count=0
for i in range(0,len(arr)):
    for j in range(1,len(arr)-1):
        if arr[i]+arr[j]==sum:
            count+=1
            
print(count)