import re

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
    f = open("User_Data.txt", 'r')
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
    invalid = True
    print("             REGISTER   ")
    print("Please create your name (should be 6 to 20 characters long) and password (should be 6 to 20 characters long, minimum one lowercase, one uppercase letter and minimum one number)")
    name = str(input("Name: "))
    password = str(input("Password: "))
    f = open("User_Data.txt", 'r')
    info = f.read()
    if name in info:
        return "Name Unavailable. Please Try Again"
    invalid = True
    if len(password) < 8:
        print('Password does meet the minimum length requirements of 8 characters.')
        invalid = False
    if len(password) > 20:
        print('Password should not exceed 20 characters.')
        invalid = False
    if not any(char.islower() for char in password):
        print('Password should have at least one lowercase letter.')
        invalid = False
    if not any(char.isupper() for char in password):
        print('Password should have at least one uppercase letter.')
        invalid = False
    if not any(char.isdigit() for char in password):
        print('Password should have at least one number.')
        invalid = False
    if invalid != False:
        f.close()
        f = open("User_Data.txt", 'w')
        info = info + " " + name + " " + password
        f.write(info)
        print("Your account is created! You can Log in now!")
    if invalid == False:
        return("Password is not valid. PLease try again.")
        return register()

def iscorrect():
    invalid = True
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

    if len(password) < 8:
        print('Password does meet the minimum length requirements of 8 characters.')
        invalid = False

    if len(password) > 15:
        print('Password should not exceed 15 characters.')
        invalid = False
    if not any(char.islower() for char in password):
        print('Password should have at least one lowercase letter.')
        invalid = False

    if not any(char.isupper() for char in password):
        print('Password should have at least one uppercase letter.')
        invalid = False
    if not any(char.isdigit() for char in password):
        print('Password should have at least one number.')
        invalid = False

    if not any(char in symbols for char in password):
        print('Password should have at least one of the symbols: !@#$%^&*() ')
        invalid = False
    if invalid:
        return invalid
 
print(choices())

