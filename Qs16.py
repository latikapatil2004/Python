'''Question 16: Write a Java program to calculate the average of all elements present in an integer array.
Asked In Practice assignment
Input Array:
[10, 20, 30, 40, 50]
Output:
Average of array elements = 30
Explanation
? The average of array elements is calculated by:
Average=Sum of all elementsNumber of elements\text{Average} = \frac{\text{Sum of all elements}}{\text{Number of elements}}Average=Number of elementsSum of all elements
? First, iterate through the array and add all elements to a variable sum.
? Then divide sum by the total number of elements (array.length) to get the average.

lightbulb Take a Help'''



arr=[10, 20, 30, 40, 50]
sum=0

for i in range(0,len(arr)):
    sum=sum+arr[i];
avg=sum//len(arr)

print("Average of array elements",avg)