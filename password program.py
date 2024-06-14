print("WELCOME TO MOBILE PASSWORD SETTING")
cp = str(input("Enter the password to create: "))
dp = str(input("Reenter the password to confirm: "))

if cp == dp:
    print("Congrats...! Your new password is:", cp)
else:
    print("Password mismatched")
attempts = 0

while attempts < 5:
    np = str(input("Enter the password to login: "))
    if cp == np:
        print("Welcome to desktop")
        break
    else:
        attempts += 1
        if attempts == 5:
            print("You have reached the maximum number of attempts.")
        else:
            print("Wrong password")
