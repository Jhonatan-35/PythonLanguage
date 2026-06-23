#Three different numbers are loaded via keyboard. Show the largest of them on the screen.

num1 = int ( input("Enter the fist value: "))
num2 = int ( input("Enter the second value:"))
num3 = int ( input("Enter the Third value :"))

if num1 >num3:
    print(num1)
    
    if num2 >num1:
      print(num2)

    else:
       print(num3)
else:
    if num2 > num3:
       print(num2)

    else:
       print(num3)
   


