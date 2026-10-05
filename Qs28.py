'''Question 28: Write a java program to find the union array of two unsorted arrays.
Asked In Practice assignment
Input:
Array1 = [1, 2, 3]
Array2 = [2, 3, 4, 5]

Output:
Union Array = [1, 2, 3, 4, 5]

Explanation:
Combine both arrays and remove duplicate elements so that each value appears only once.'''



arr1=[1, 2, 3]
arr2=[2, 3, 4, 5]
nums=([0]*len(arr1))*len(arr2);
k=0
for i in range(len(arr1)):
    nums[k]=arr1[i];
    k=k+1
    
for i in range(len(arr2)):
    found=False;
    if nums[k]==arr2[i]:
        found=True;
        break;
        
    if found==False:
        
        nums[k]=arr2[i];
        k=k+1
     
for j in range(len(nums)):
    print(nums)
      
 