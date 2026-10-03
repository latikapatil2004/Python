'''Question 3: Write a java program to print all alphabets from a to z. - using while loop
Asked In Just Practice assignment
Input:

No input required

Output:

a b c d e f ... z

Explanation:

The program starts from character ‘a’ and prints each character until ‘z’.
The loop increments the character in every iteration.'''


ch='A'
while ch<='Z':
    print(ch)
    ch=chr(ord(ch)+1)