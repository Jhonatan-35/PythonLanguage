#Make a program that reads four numerical values and report their sum and average

value1 = int (input("Enter the first value :"))
value2 = int (input("Enter the second value :"))
value3 = int (input("Enter the third value :"))
value4 = int (input("Enter the four value :"))

sum = value1 + value2 +value3 + value4
average = sum /4
print(f'The sum of the values is : {sum}')
print(f'The average of teh avalues is : {average}')