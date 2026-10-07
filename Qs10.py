'''9.Find the Product of All Elements
Write a Python program to create a set of integers and calculate the product of all elements.'''




set={1,2,3,4,5,6}
product=1
for num in set:
    product=product*num
    
print("Product of all elements",product)
    