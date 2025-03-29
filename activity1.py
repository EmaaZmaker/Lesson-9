medical_condition=input("enter your medical condition")
attendance=int(input("enter your attendance"))
if medical_condition=="yes":
    print("you are allowed")
else:
    if attendance>=75:
        print("you are allowed")
    else:
        print("you are not allowed")
    