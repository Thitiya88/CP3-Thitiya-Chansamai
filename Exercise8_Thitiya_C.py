usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput == "kratai" and passwordInput == "12345":
    print("Welcome to rabbit shop")
    print("-----Menu-----")
    print("1.lays  20THB")
    print("2.donut 15THB")
    print("3.water 10THB")
    userSelected = int(input("Please select number:"))
    if userSelected == 1:
        quantity1 = int(input("quantity:"))
        print("Total:",quantity1*20,"THB")
    elif userSelected == 2:
        quantity2 = int(input("quantity:"))
        print("Total:", quantity2*15, "THB")
    elif userSelected == 3:
        quantity3 = int(input("quantity:"))
        print("Total:",quantity3*10, "THB")
    else:
        print("wrong number, please try again")
    print("------Thank you------")
else:
    print("Failed")





