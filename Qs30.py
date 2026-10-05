'''Question 31: Replace First and Last Element with 0.
Asked In Practice assignment
Input:
Array = [5, 3, 7, 2]

Output:
Array = [0, 3, 7, 0]

Explanation:
Update the first and last positions of the array with 0 and leave the middle elements unchanged.'''


nums=[5, 3, 7, 2]
nums[0]=0
nums[len(nums)-1]=0
  
print(nums)
        
        