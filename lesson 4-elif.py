#elif- allows us to test more than one condition
maths = float(input("Enter your maths score"))
if maths >=100:
    print("Invalid score")
elif maths <0 :
    print("Invalid score. Score cannot be less than 0")
elif maths >=70 :
    print("scored an A")
elif maths >=60:
    print("Scored a B")
elif maths >=50:
    print("Scored a C")
elif maths <50:
    print("You failed. You can do better")
else:
    print("Contact your teacher")

eng = float(input("Enter your english score"))
if eng >= 70 and eng <= 100:
    print("You scored an A")
elif eng >=60 and eng < 70:
    print("You scored a B")
elif eng >= 50 and eng <60:
    print( "C")
elif eng >=0 and eng <50:
    print("You failed")
elif eng <0 :
    print("Invalid entry")
else:
    print("Contact your teacher")


