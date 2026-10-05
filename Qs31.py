'''Question 34: Return the first element that repeats in the array.
Asked In Practice assignment
Input:
Array = [10, 5, 3, 4, 3, 5, 6]

Output:
First repeating element = 5

Explanation:
Check elements from left to right and identify the element whose first occurrence appears earlier but repeats later in the array.

lightbulb Take a Help'''

arr=[10, 5, 3, 4, 3, 5, 6]
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)-1):
        
       if arr[i]==arr[j]:
           print(arr[i]);   
           break;
else:
    continue    
    

     
    
    

