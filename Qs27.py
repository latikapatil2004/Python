'''Question 27: Write a java program to count the frequency of each element in a given array.
Asked In Practice assignment
Input:
Array = [1, 2, 2, 3, 3, 3, 4]

Output:
1 ? 1 time
2 ? 2 times
3 ? 3 times
4 ? 1 time

Explanation:
For each element in the array, count the number of occurrences by comparing it with all other elements.

lightbulb Take a Help'''



arr=[1, 2, 2, 3, 3, 3, 4]
for i in range(0,len(arr)):
    found=False
    for j in range(0,len(arr)):
        if arr[i]==arr[j] :
            found=True;
            break
            
        if found:
            continue
        count=0
            
for i in range(len(arr)):
    if arr[i]==arr[j]:
        count+=1
    
    print(f"{arr[i]} :{count} times")
            
            
            