'''
7.Add Corresponding Elements from Two Sets
Write a Python program to create two sets containing the same number of elements. Convert them into 
lists and calculate the sum of corresponding elements.
Sample Input:
Set 1 = {10, 20, 30}
Set 2 = {1, 2, 3}
Sample Output:
11
22
33'''

Set1 = {10, 20, 30}
Set2 = {1, 2, 3}

list1=list(Set1)
list2=list(Set2)
for i in range (0,len(list1)):
    print(list1[i]+list2[i])