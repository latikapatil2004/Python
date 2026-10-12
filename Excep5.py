'''Q5. Using finally
Write a Python program to divide two numbers and display "Program Completed" using the finally block, whether an exception occurs or not.

'''


try:
    a=int(input("entr no"))
    b=int(input("ente no"))
    print("Division ",a//b)
    
    
except Exception as e:
    print("Exception is ",e)
    
finally:
    print("program completed")
    