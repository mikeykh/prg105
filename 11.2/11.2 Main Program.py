# import the productionworker module
import employee

# get input form user
name = input("Enter Employee Name: ")
number = input("Enter Employee Number: ")
shift = input("Enter Shift number (Enter 1 for day and 2 for night): ")
pay_rate = input("Enter Hourly Pay Rate: ")

# initialize using the ProductionWorker class from the employee module
my_employee = employee.ProductionWorker(name, number, shift, pay_rate)

# print the information entered by the user
print("\n--------------------")
print("Employee Information")
print("--------------------")
print(my_employee)
