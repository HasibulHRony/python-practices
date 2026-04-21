

# open("employee.txt", "a")
# open("employee.txt", "r")
# open("employee.txt", "w")
# open("employee.txt", "r+")

employee_file = open("employee.txt", "r")


# print(employee_file.readable())


print(employee_file.readline())
print(employee_file.readline())
print(employee_file.readlines()[1])
for employee in employee_file.readlines():
    print(employee)
employee_file.close()