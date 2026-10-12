'''Q1. Division of Two Numbers
Write a Python program to divide two numbers. Handle the exception that occurs when the denominator is zero'''

try:
    a=10;
    b=0;
    print("Division iis:",a//b)
except ZeroDivisionError as a:
    print("Error ",a)
    