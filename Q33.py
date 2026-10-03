'''Question 6: Write a Java program to check whether a character is alphabetic or not.
Asked In Just Practice assignment
Input:
Character = A

Output:
Alphabet

Explanation:
If character lies between A–Z or a–z.'''

ch=input("enter alphabet")
if ch>='A' or ch<='Z':
    print("Alphabet")
else:
    print("not alphabet")