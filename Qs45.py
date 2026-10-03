'''uestion 21: Write a java program to check Number Is Prime Number or Not.
Example : A prime number is a number that can only be divided by itself and 1 without remainders.The prime numbers from 1 to 100 are: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97.
Asked In Just Practice assignment
Input:

Number = 7

Output:

Prime Number

Explanation:'''


number=int(input("enter number"))
count=0
for i in range(1,number+1):
    if number%i==0:
        count=count+1
     
if count==2:
    print("Number is prime")
else:
    print("number not prime")