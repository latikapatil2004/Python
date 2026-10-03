'''Question 22: Write a java program to Check Number Is Perfect Number or Not.
Example : perfect number, a positive integer that is equal to the sum of its proper divisors. The smallest perfect number is 6,which is the sum of 1, 2, and 3. Other perfect numbers are 28, 496, and 8,128.
Asked In Just Practice assignment
Input:

Number = 6

Output:

Perfect Number

Explanation:

Proper divisors of 6 are 1, 2, and 3.
Sum = 1 + 2 + 3 = 6.
Since the sum equals the number, it is a Perfect Number.'''


number=int(input("enter the number"))
temp=number
sum=0
for i in range(1,number):
    if number%i==0:
        sum=sum+i
if sum==temp:
    print("perfect no")
else:
    print("not perfect")