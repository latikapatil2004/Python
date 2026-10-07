'''10.Find Common Even Numbers

Write a Python program to create two sets and display the common elements that are even numbers.
Sample Input:
Set 1 = {2, 3, 4, 5, 12, 35}
Set 2 = {1,2,5,4,6,12}
Sample Output:
2
4
12'''


Set1 = {2, 3, 4, 5, 12, 35}
Set2 = {1,2,5,4,6,12}
for num in Set1:
    if num in Set2 and num%2==0:
        print(num)

