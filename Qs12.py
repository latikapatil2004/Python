'''
Question 12: Write a Java program to calculate simple interest.
Asked In Basic program
Input:
Principal = 1000
Rate = 5
Time = 2

Output:
Simple Interest = 100

Explanation:
Simple Interest formula:
SI = (Principal * Rate * Time) / 100
Applying the formula gives 100.

lightbulb Take a Help'''

principle=int(input("Enter principle \n"))
rate=int(input("Enter rate \n"))
time=int(input("Enter time \n"))
simple_intrest=(principle*rate*time)/100
print("Simple intrest : ",simple_intrest)