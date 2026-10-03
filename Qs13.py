'''Question 13: Write a Java program to calculate compound interest.
Asked In Basic program
Input:
Principal = 2000
Rate = 10
Time = 2

Output:
Compound Interest = 420

Explanation:
Compound Interest is calculated using the formula:
CI = P(1 + R/100)^T ? P
After calculation, the compound interest is 420.

lightbulb Take a Help'''

principle=int(input("Enter principle \n"))
rate=int(input("Enter rate \n"))
time=int(input("Enter time \n"))
compound_interest = principle * (1 + rate/100) ** time - principle
print("Simple intrest : ",compound_interest)