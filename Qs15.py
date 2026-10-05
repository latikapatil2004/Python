'''Question 15: Write a java program to find common elements between two arrays.
Asked In Practice assignment
Input :
Array1 = {1, 2, 3, 4, 5}
Array2 = {3, 4, 5, 6, 7}
Output : Common elements = {3, 4, 5}
Explanation :
Compare each element of Array1 with all elements of Array2, if match found ? it is a common element.

lightbulb Take a Help'''



arr1=[1, 2, 3, 4, 5]
arr2=[3, 4, 5, 6, 7]
for i in range(0,len(arr1)):
    for j in range(0,len(arr2)):
        if arr1[i]==arr2[j]:
            print(arr1[i])
        
        
    
       