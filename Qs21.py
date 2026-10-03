'''Question 21: Write a Java program to reverse a number without using a loop.
Asked In Basic program
Input:
123

Output:
321

Explanation:
Digits are separated using arithmetic operations and rearranged in reverse order without using loops.'''

num=int(input("enter value"))
rev=(num%10)*100+((num//10)%10)*10+(num//100)
print("Reverse : ",rev)