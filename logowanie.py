def choices():
    choice = int(input("For Sign In type 1 and for Register type 2: "))
    if choice == 1:
        return signin()
    elif choice == 2:
        return register()
    else:
        print("Bad number, type 1 or 2.\n")
        return choices()


def signin():
    print("           SIGN IN   ")
    print("Please type your name and password")
    name = str(input("Name: "))
    password = str(input("Password: "))
    f = open("User_Data.txt",'r')
    info = f.read()
    info = info.split()
    if name in info:
        index = info.index(name) + 1
        usr_password = info[index]
        if usr_password == password:
            return "Hello! Welcome Back, " + name
        else:
            print("!!!Password is wrong, try again!!!\n")
            return signin()
    else:
        return "Name not found. Please Sign Up."

def register():
    print("             REGISTER   ")
    print("Please create your name and password")
    name = str(input("Name: "))
    password = str(input("Password: "))
    f = open("User_Data.txt",'r')
    info = f.read()
    if name in info:
        return "Name Unavailable. Please Try Again"
    f.close()
    f = open("User_Data.txt",'w')
    info = info + " " +name + " " + password
    f.write(info)
    print("Your account is created")







print(choices())

















