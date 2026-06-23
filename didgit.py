#A positive one- or two-digit number is entered via keyboard (1..99) and a message is displayed indicating whether the number has one or two digits
#Take into account what condition must be met to have two digits of an integer

digit = int(input("Enter 1- digit or 2- digit :"))

if digit < 10:
    print("The number has one digit")

else:
    print("The number has two digits")