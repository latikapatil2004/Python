'''Question 14: Write a java program to remove duplicated values from arrays.
Asked In Practice assignment
Input : Array = {10, 20, 20, 30, 40, 40, 50}
Output : Unique elements = {10, 20, 30, 40, 50}
Explanation:
Traverse the array, check if element already exists before adding to result, thus avoiding duplicates.'''



arr=[10, 20, 20, 30, 40, 40, 50]
for i in range(0,len(arr)):
    found=True
    for j in range(0,i):
        if arr[i]==arr[j]:
            found=False
            break            
    if found :
        print(arr[i])

   