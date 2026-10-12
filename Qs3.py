'''.Find the Maximum Element
Write a Python program to create a set of integers and find the largest element in the set.
'''


s={10,20,30,40,50}
largest=0
for num in s:
    if(num>largest):
        largest=num
        
        
print("LArgest",largest)