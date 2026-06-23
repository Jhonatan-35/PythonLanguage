#Three values are entered per keyboard, if they are all the same, the sum of the first with the second is printed and this result is multiplied by the third.
num1 = int (input("Enter the first Number:"))
num2 = int (input("Enter the second Number"))
num3 = int (input("Enter the Thrid Number"))


if num1 ==num2 and num1==num3:
    sum = num1 +num2 
    print(f'The sum of the two products is {sum}:')
    product = sum * num3
    print(f'The Multyply of the products{product}')
    
