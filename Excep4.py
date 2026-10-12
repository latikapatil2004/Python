'''Q4. Multiple Exceptions
Write a Python program to accept two numbers and divide them. Handle both ValueError and ZeroDivisionError.
'''

try:
    a=int(input("Enter no"));
    b=int(input("enter no"));
    print("Division is",a//b);
except ZeroDivisionError as z:
    print("Error ",z);
    
    
except ValueError as v:
    print("Error is ",v)
