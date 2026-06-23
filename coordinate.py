#Write a program that asks to enter the coordinate of a point in the plane, that is, two integer values x and y (other than zero).
#Subsequently print on the screen in which quadrant said point is located. (1st Quadrant if x > 0 Y and > 0 , 2nd Quadrant: x < 0 Y and > 0, etc.)

x = int(input("Enter the point plane of X :" ))
y = int(input("Enter the point plane of Y :"))
if x >0 and y >0:
    print("The localated in first quadrant")

else:
    if x< 0 and y>0:
        print ("The localated in second quadrant")
    else:
        if x<0 and y<0:
            print("The localated in thrid quadrant")
        else:
            print("The localated in  fourth quadrant")
