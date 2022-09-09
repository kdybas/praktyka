l, u, p, d = 0, 0, 0, 0
s = "R@m@_f0rtu9e$"
capitalalphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
smallalphabets="abcdefghijklmnopqrstuvwxyz"
specialchar="$@_"
digits="0123456789"
def choices():
    try:
        choice = str(input("For Sign in type 1 and for Register type 2: "))
        if int(choice) == 1:
            return signin()
        elif int(choice) == 2:
            return register()
        elif int(choice)>2 or int(choice)<1:
            print("Bad number, you can type only 1 or 2.\n")
            return choices()
    except:
        print("You can only type number 1 or 2. You can't type character's\n")
        return(choices())


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
    print("Please create your name and password. Name must be 4 letters minimum. Password must be 8 letters minimum")
    name = str(input("Name: "))
    password = str(input("Password: "))
    f = open("User_Data.txt",'r')
    info = f.read()
    if name in info:
        return "Name Unavailable. Please Try Again"
    if len(name)<4:
        print("Name must be 4 letters minimum. Please try Again")
        return register()
    print(is_valid_password(password))
    f.close()
    f = open("User_Data.txt",'w')
    info = info + " " +name + " " + password
    f.write(info + "\n")
    return("Your account is created, you can sign in now! :)\n")



def is_valid_password(password):
    MIN_SIZE = 6
    MAX_SIZE = 20
    password_size = len(password)
    if password_size < MIN_SIZE:
        print("Password must be 6 letters minimum and 20 letters maximum. Please try again.")
        return register()
    elif password_size > MAX_SIZE:
        print("Password must be 6 letters minimum and 20 letters maximum. Please try again.")
        return register()

print(choices())

















