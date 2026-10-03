'''Question 23: Write a Java program to calculate the sum of the first and last digit without using a loop.
Asked In Basic program
Input:
123

Output:
4

Explanation:
First digit = 1
Last digit = 3
Sum = 1 + 3 = 4.'''


num=int(input("Enter number"))
first=num//100
last=num%10
print("sum of first and last digit :",first+last)
