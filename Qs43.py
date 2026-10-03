'''Question 17: Write a java program to find all factors of a number.
Asked In Just Practice assignment
Input:

Number = 12

Output:

Factors: 1 2 3 4 6 12

Explanation:

A factor divides the number completely without remainder.
All numbers that divide 12 exactly are printed.

lightbulb Take a Help'''


number=int(input("Enter the number"))
for i in range(1,number+1):
    if(number%i==0):
        print(i)
        