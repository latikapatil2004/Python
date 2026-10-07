'''Q.8
Simple Login System
Write a Python program to create a ictionary containing usernames and passwords. 
Ask the user to enter a username and password and check whether the login details are correct.

Q.9
Subject Marks
Write a Python program to take subject names and marks for three subjects and store them in a dictionary
Display all subjects and marks and calculate the average marks.


Q.10
Word Frequency
Write a Python program to take a sentence from the user and store each word and its frequency in a 
dictionary. Display the resulting dictionary.'''


dict={}
sum=0
for i in range(3):
    subject=input("Enter subject name :")
    marks=int(input("enter marks"))
    dict[subject]=marks
    
for val in dict.values():
    sum=sum+val
    
print("Average marks",sum//3)