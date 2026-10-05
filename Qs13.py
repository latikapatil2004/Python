'''Question 13: Write a java program to display only non-zero values from an array.
Asked In Practice assignment
Input : Array = {1, 0, 5, 0, 7, 0, 9}
Output : Non-zero elements = {1, 5, 7, 9}
Explanation :
Traverse the array and print only elements that are not equal to zero.'''


arr=[1, 0, 5, 0, 7, 0, 9]
for i in range(0,len(arr)):
    if arr[i]!=0:
        print(arr[i],end=" ")
        