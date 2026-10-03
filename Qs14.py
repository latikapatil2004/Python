'''Question 14: Write a Java program to swap two numbers using a third variable.
Asked In Basic program
Input:
A = 5
B = 10

Output:
A = 10
B = 5

Explanation:
A temporary variable is used to store one value while swapping the numbers.

lightbulb Take a Help'''

a=int(input("enter A : "))
b=int(input("enter B : "))
c=a
a=b
b=c
print("A :",a)
print("B :",b)