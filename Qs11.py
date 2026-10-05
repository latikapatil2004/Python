'''Question 11: Write a java program to give an array, find the second largest element.
Asked In Practice assignment
Input : Array = {12, 35, 1, 10, 34, 1}
Output : Second largest = 34
Explanation:
First largest is 35, second largest is the next maximum (34). We maintain two variables (largest, secondLargest).'''


arr=[12,35,1,10,34,1]
largest=arr[0]
secondLargest=arr[0];
for i in range(0,len(arr)):
    if arr[i]>largest:
        largest=arr[i]

for i in range(0,len(arr)):
    if arr[i]>secondLargest and arr[i]<largest:
        secondLargest=arr[i]
       
     

print("secondlargest",secondLargest)


