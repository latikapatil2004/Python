'''.3
Phone Book
Write a Python program to take a person's name and phone number as input and store them in a dictionary.
Ask the user for a name and display the corresponding phone number.'''



name=input("Enter name")
phone=int(input("Enter phone no"))
dict={}
dict[name]=phone
search=input("Enter Name")
print("Phone no :", dict[search])