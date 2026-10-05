'''uestion 20: Write a Java program to print all elements from an integer array that are greater than a given number.
Asked In Practice assignment
Input:
Array = [10, 25, 5, 40, 18]
Given Number = 20

Output:
Elements greater than 20: 25 40

Explanation:
Traverse the array and compare each element with the given number; if the element is greater than the number, print it.'''


arr=[10,25,5,40,18]
val=20
for i in range(0,len(arr)):
    if arr[i]>val:
        print(arr[i])
        