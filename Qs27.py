'''Question 27: Write a Java program to toggle the case of an alphabet using ASCII values.
Asked In Basic program
Input:
a

Output:
A

Explanation:
Lowercase and uppercase letters differ by 32 in ASCII values.
By adding or subtracting 32, the case of the alphabet can be changed'''

a=input("enter character")
toggle=a-32
print("Toggle case :",toggle)