'''Question 24: Write a Java program to check whether a number is a Neon number or not.
Asked In Basic program
Input:
9

Output:
Neon Number

Explanation:
A Neon number is a number where the sum of digits of its square is equal to the number itself.
9^2 = 81 ? 8 + 1 = 9.'''


num=int(input("enter num\n"))
square=num*num
sum=0
while square>0:
    rem=square%10
    sum=sum+rem
    square=square//10
    
if num==sum:
    print("Neon number")
else:
    print("not neon")
    
    
    