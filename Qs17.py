'''
Q.6
Student Grade Dictionary
Write a Python program to take a student's name and percentage as input. Store the student's name and 
grade in a dictionary based on the following criteria:
75 and above → A
60 to 74     → B
40 to 59     → C
Below 40     → Fail
'''



dict={}
for i in range(4):
    name=input("Enter your name : ")
    percentage=int(input("Enter percentage"))
    dict[name]=percentage
    
    
for key,val in dict.items():
    if val>=75:
        print("A")
        
    elif val>=60 and val<=74:
        print("B")
        
    elif val>=40 and val<=59:
        print("C")
        
    else:
        print("Fail")
        
        