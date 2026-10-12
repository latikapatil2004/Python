'''3. Find the Minimum Element
Write a Python program to create a set of integers and find the smallest element in the set.
'''


s={1,3,4,5,6,7,8}
min=s('inf');
for num in s:
    if num<min:
        min=num
        
print("Minimum",min)