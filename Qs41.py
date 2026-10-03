'''
Question 15: Write a java program to print all ASCII characters with their values.
Asked In Just Practice assignment
Input:

No input required

Output (Sample):

A = 65
B = 66
...

Explanation:

The program uses a loop from 0 to 127.
Each number is converted to its corresponding character and printed.

lightbulb Take a Help
Each division reduces one digit, and a counter keeps track of total digits.
'''

i=1
while i<=127:
    print(chr(i),"=", i)
    i=i+1

