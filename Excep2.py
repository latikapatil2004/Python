'''Q2. Integer Input
Write a Python program to accept an integer from the user. Handle the exception if the user enters a non-numeric value.
'''

try:
    a=int(input("enter number"));
except ValueError as v:
    print("Error ee",v);
    