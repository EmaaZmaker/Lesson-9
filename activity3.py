print("select your ride")
print("1.bike")
print("2.car")
choice=int(input("enter your choice"))
if choice==1:
    print("which type of bike do you want?")
    print("1.scooty")
    print("2.scooter")
    choice1=int(input("enter your choice"))
    if choice1==1:
        print("you got scooty")
    else:
        print("you got scooter")
elif choice==2:
    print("which type of car do you want?")
    print("1.SUV")
    print("2.Sedan")
    choice1=int(input("enter your choice"))
    if choice1==1:
        print("you got SUV")
    else:
        print("you got Sedan")
    