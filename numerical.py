num1 = int (input("Write the 1st number : "))
num2 = int (input("Write the 2nd number : "))
num3 = int (input("Write the 3er number : "))

if num1 < num2 and num1 < num3:
    print(num1)

else :
    if num2 < num3:
        print(num2)
    else:
        print(num3)
if num1 > num2 and num1 >num3:
    print(num1)
else :
    if num2 > num3:
        print (num2)
    else:
        print(num3)


