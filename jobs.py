totalquestion = int(input("What is the total questions asked : "))
totalanswered = int(input("What is the total question aswered correctly: "))
percentage = totalanswered * 100/totalquestion

if percentage >=90 :
    print("Your level is maximun")
 
else:
    if percentage >=75:
        print("Your level is avaerage:")

    else:
        if  percentage>=50:
            print("Your level is Regular")
        else:
            print( "Your level off")
