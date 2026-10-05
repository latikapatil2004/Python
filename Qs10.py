'''uestion 10: Write a program in java to delete an element at desired position from an array.
Asked In Practice assignment
Input the size of array : 5

Input 5 elements in the array in ascending order :
1 2 3 4 5

Input the position where to delete : 3

Expected Output : The new list is : 1 2 3 5'''


arr=[1,2,3,4,5]
pos=3
for i in range(pos-1,len(arr)-1):
    arr[i]=arr[i+1]
    
for i in range(len(arr)-1):
    print(arr[i],end=" ")