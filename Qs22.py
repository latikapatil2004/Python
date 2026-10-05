'''Question 22: Write a Java program to check whether two integer arrays are equal.
Two arrays are considered equal if:
Asked In Practice assignment
Input:
Array1 = [10, 20, 30, 40]
Array2 = [10, 20, 30, 40]

Output:
Arrays are equal.

Explanation:
First compare the lengths of both arrays and if they are equal then compare elements at each index; if all elements match the arrays are equal otherwise they are not.'''


Array1 = [10, 20, 30, 40]
Array2 = [10, 20, 90, 40]
found=True
for i in range(0,len(Array1)):
    if Array1[i]!=Array2[i]:
        found=False
        break
       
if found==True:
    print("arrays are equal")
else:
    print("Array not equal")