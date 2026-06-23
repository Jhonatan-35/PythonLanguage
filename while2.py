#Encode a program that requests the loading of a positive value and shows us from 1 to the value entered one by one.
#Example: If we enter 30, the numbers from 1 to 30 must be displayed on the screen.
"""
n = int (input("Enter your value :"))
x =1
while x<=n:
    print(x)
    x = x+1
"""
#Develop a program that allows the loading of 10 values per keyboard and subsequently shows us the sum of the values entered and their average.

x=1
sum = 0
while x<=10:
    valor = int (input("What is your valor ?"))
    sum = sum +x
    x = x+1
    average = sum /10
    print(sum)
    print(average)

