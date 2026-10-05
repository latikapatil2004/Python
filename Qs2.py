'''Question 2: Write a Java program to calculate the sum of all elements in an array.
Asked In Practice assignment
Input:
Array Size = 5
Array Elements = 2 4 6 8 10
Output:
Sum of array elements = 30
Explanation:
? Initialize a variable sum = 0.
? Traverse the array and keep adding each element to sum.
? After the loop ends, sum will hold the total of all array elements.'''


list=(2,4,6,8,10)
i=0
sum=0
l=(len(list))
for i in range(i,l):
    sum=sum+list[i]

print("sum ",sum)