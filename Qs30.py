'''uestion 2: Write a Java program to check whether a triangle is valid or not.
Asked In Just Practice assignment
Input:
A = 5, B = 6, C = 7

Output:
Valid Triangle

Explanation:
A triangle is valid if the sum of any two sides is greater than the third side.

lightbulb Take a Help'''
 
A=int(input("enter the value\n"))
B=int(input("enter the value\n"))
C=int(input("enter the value\n"))
if A+B==C:
    print("Valid Triangle")
else:
    print("not valid triangle")