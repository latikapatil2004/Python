'''Question 3: Write a Java program to display even & odd values from an array.
Asked In Practice assignment
Input:
Array Size = 6
Array Elements = 11 20 33 42 55 60
Output:
Even Values = 20 42 60
Odd Values = 11 33 55
Explanation:
? Traverse the array element by element.
? If an element is divisible by 2, it is even. Otherwise, it is odd.
? Separate lists are displayed for even and odd values'''


list=[11,20,33,42,55,60]
l=len(list)
print("Even values")
for i in range(0,l):
    if list[i]%2==0:
        print(list[i],end=" ")
        
print("\nOdd values")
for i in range(0,l):
    if list[i]%2!=0:
        print(list[i],end=" ")
