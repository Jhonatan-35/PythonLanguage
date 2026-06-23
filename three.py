#Three numbers are entered by keyboard, if at least one of the values entered is less than 10, print the legend "Some of the numbers are less than ten" on the screen.

num1 = int (input("Enter the first Number: "))
num2 = int (input("Enter the second Number: "))
num3 = int (input("Enter the Thrid Number: "))

if num1 <10 or num2<10 or num3<10:
    print("Some numbers is less ten")

