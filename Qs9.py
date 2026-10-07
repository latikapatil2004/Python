'''8.Find the Difference Between Maximum and Minimum
Write a Python program to create a set of integers and calculate the difference between the maximum and
minimum elements.'''



set={1,2,3,5,6,7,5,3,10}
max=0
min=0
for num in set:
    if num>=max:
        max=num
        
for num in set:
    if num<=min:
        min=num
        
        
print("Diffrence between max and min ", max-min)
                
        
        