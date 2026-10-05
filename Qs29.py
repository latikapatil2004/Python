'''Question 30: Replace All Elements Divisible by 3 with -1.
Asked In Practice assignment
Input:
Array = [3, 6, 7, 9, 10]

Output:
Array = [-1, -1, 7, -1, 10]

Explanation:
Traverse the array and if an element is divisible by 3 replace it with -1 while keeping other elements unchange'''



arr=[3, 6, 7, 9, 10]
for i in range(0,len(arr)):
    if arr[i]%3==0:
        arr[i]=-1
       
       
print(arr)