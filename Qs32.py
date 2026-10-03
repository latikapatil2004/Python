'''Question 5: Write a Java program to check whether a number is divisible by 5 and 11 or not.
Asked In Just Practice assignment
Input:
Number = 55

Output:
Divisible by 5 and 11

Explanation:
If number % 5 == 0 AND number % 11 == 0'''

number=int(input("enter the values"))
if number%5==0 and number%11==0:
    print("divisible by 5 and 11")
else:
    print("not divisible")