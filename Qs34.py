'''Display a menu to perform the following operations without using switch or match-case:

Add Employee

View Employee

Search Employee

Exit'''

employee=((201,"Latika",23455),
         (201,"Latika",23455,));
while True:
    print("\n----- Employee Management Menu -----")
    print("1. Add Employee")
    print("2. View Employee")
    print("3. Search Employee")
    print("4. Exit")
    choice=int(input("Enter choice"))
    if choice=="1":
        emp_id=int(input("Enter id "));
        emp_name=input("Enter name");
        salary=int(input("Enter salary"));
        employee.append(emp_id,emp_name,salary)
    elif choice=="2":
        for emp in employee:
            print("Employee_id",emp[0],"\t","Employee_name",emp[1],"\t","Employee_salary",emp[2]);
  
        
    
    
