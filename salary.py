#Calculate the monthly salary of an operator knowing the number of hours worked and the value per hour
hoursworked = int (input("Enter the hours worked by operartor: "))
valueperhour = int (input("Enter The value per hour: "))

salary = hoursworked * valueperhour
print(f'The salary total worked by operator is : {salary}')