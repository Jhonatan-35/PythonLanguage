#An integer value is entered via keyboard, displaying a legend indicating whether the number is positive, negative or null (i.e. zero)
num = int (input("Enter the number:"))

if num ==0:
    print("Your entered  was entered zero")

else:
    if num >0:
        print("Your entered Positive:")

    else:
        print("You entered Negative Number")