'''Question 24: Write a program in java to rotate an array by N positions ?
Asked In Practice assignment
Input:
Array = [0, 3, 6, 9, 12, 14, 18, 20, 22, 25, 27]
Position = 4

Output:
Rotated Array = [12, 14, 18, 20, 22, 25, 27, 0, 3, 6, 9]

Explanation:
Split the array into two parts at the given position and place the second part first followed by the first part to complete the rotation.'''



arr=[0, 3, 6, 9, 12, 14, 18, 20, 22, 25, 27]
pos=4;
nums=[0]*len(arr)
j=0
for i in range(pos,len(arr)):
    nums[j]=arr[i];
    j=j+1
    
for i in range(0,pos):
    nums[j]=arr[i];
    j=j+1
    
   
print(nums)
 
   
    
    
