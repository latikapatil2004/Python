


from collections import namedtuple
Employee = namedtuple(
    "Employee",
    ["id", "name", "role"]
)
employee=Employee(1,"john","devloper")
print(employee.name)
employee.id
employee.role