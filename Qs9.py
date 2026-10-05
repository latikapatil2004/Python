'''Question 9: Write a java program to copy one array to another array.
Asked In Practice assignment
Input : Array1 = {5, 10, 15, 20}
Output : Array2 = {5, 10, 15, 20}
Explanation:
Copy each element of Array1 into Array2 using index-by-index assignment'''


arr=[5,10,15,20]
nums=[0,0,0,0]
for i in range(0,len(arr)):
    nums[i]=arr[i]
print(nums)
    