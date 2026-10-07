'''Q.4
Product Price List
Write a Python program to take the names and prices of three products and store them in a dictionary. 
Display all product names and their prices.
'''


dict={}
for i in range(3):
    name=input("Enter name")
    prices=int(input("Enter prices"))
    dict[name]=prices
for key,val in dict.items():
    print(key,val)