num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the Third number: "))

print("The largest number is :")

if num1>num2 and num1 >num3:
    print(num1)
else:
    if num2 >num3:
        print(num2)

    else:
        print(num3)


