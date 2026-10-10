'''21. Write a Python program to create an Employee Data Management System using a List and Tuple to store employee details (empid, Ename, Esal). Initially, store the following employee records:

[(201, 'Rahul', 45000), (202, 'Priya', 52000)]

'''


employees = (
    (201, 'Rahul', 45000),
    (202, 'Priya', 52000)
)

for emp in employees:
    print("Employee ID:", emp[0])
    print("Employee Name:", emp[1])
    print("Employee Salary:", emp[2])
    print("----------------------")
    
    
    