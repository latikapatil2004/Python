'''Q.7
Display the dictionary.
Country and Capital
Write a Python program to take the names of three countries and their capitals from the user and store them in a dictionary. Display all country-capital pairs.'''



dict={}
for i in range(3):
    country=input("enter country name : ")
    capital=input("enter capital name : ")
    dict[country]=capital
    
    
for key,val in dict.items():
    print(key,":",val)