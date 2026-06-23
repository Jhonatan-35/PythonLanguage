#Create a program that allows you to load a positive integer of up to three digits and display a message indicating whether it has 1, 2, or 3 digits. Display an error message if the number of digits is greater.

digit = int(input("Enter the number of two digits: "))
if digit <10:
    print("The valus has one digits")
else:
    if digit <100:
        print("The value has two digits")
    else:
        if digit <1000:
          print("The value has three digits")
        else:
          print("The error message")