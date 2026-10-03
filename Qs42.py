'''Question 16: Write a java program to find power of a number.
Asked In Just Practice assignment
Input:

Base = 2
Exponent = 3

Output:

Result = 8

Explanation:

2 raised to the power 3 means 2 * 2 * 2.
The result is 8.'''


base=int(input("enter base"))
exponent=int(input("enter exponent"))
result=1
i=1
while i<=exponent:
    result=result*base
    i=i+1
print("Result " , result)