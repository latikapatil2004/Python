'''Question 26: Write a Java program to check whether a number is a Spy number.
Asked In Basic program
Input:
1412

Output:
Spy Number

Explanation:
A Spy number is a number where the sum of digits equals the product of digits.
Sum = 1 + 4 + 1 + 2 = 8
Product = 1 * 4 * 1 * 2 = 8.'''
 
num=int(input("Enter number"))
sum=num%10+((num//10)%10)+((num//100)%10)+(num//1000)
product=num%10*((num//10)%10)*((num//100)%10)*(num//1000)
if sum==product:
    print("Spyy")
else:
    print("number is not spy")