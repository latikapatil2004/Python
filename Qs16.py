'''
Q.5
Dictionary Update
Write a Python program to create a dictionary containing three key-value pairs. 
Ask the user for a key and a new value, then update the dictionary with the new value. 
Display the updated dictionary.'''



dict={}
for i in range(3):
    name=input("enter name :")
    id=int(input("Enter id :"))
    dict[name]=id
    
    
print("Original dictionary" ,dict)  
name=input("update name")
id=int(input("Enter id "))
dict[name]=id

print("Updated dictionary: "," ")
for key,value in dict.items():
    print(key,value)
    