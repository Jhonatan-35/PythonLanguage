salary = int( input("What is your salary ? :"))
seniority = int(input("How many of señority carrying in the company ? :"))
if salary < 500 and seniority > 10:
    increase = salary * 0.20 
    total = salary + increase
    print (f'You salary total more 20% is :{total} $')
else:
    if salary < 500 and seniority < 10:
        increase = salary * 0.05
        total = salary + increase
        print(f'You total salary more 5% is : {total}$')
    else :
        print ("Your salary without changes is 500 $")
    







