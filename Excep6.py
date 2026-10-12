'''.6 Age Validation
Accept the user's age as input. Handle invalid input and display the age if it is a valid integer.
'''
    
try:
    age = int(input("Enter valid age: "))
    print("Age is:", age)

except Exception as e:
    print("Age not valid", e)