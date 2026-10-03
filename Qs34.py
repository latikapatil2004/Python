'''Question 8: Write a Java program to check whether a year is a leap year or not.
Asked In Just Practice assignment
Input:
Year = 2024

Output:
Leap Year

Explanation:
A year is leap if:

Divisible by 4

Not divisible by 100 unless divisible by 400'''

year=int(input("Enteer year"))
if year%400==0 or (year%4==0 and year%100!=0):
    print("Leap year")
    
        
else:
    print("Not leap year")
        