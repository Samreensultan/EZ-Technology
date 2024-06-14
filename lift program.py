import time
c = 0
def l(t):
    global c
    if t < 0 or t> 4:
        print("Invalid floor. Choose a floor between 0 and 4.")
    else:
        if t > c:
            print(f"Moving up to floor {t}")
            for floor in range(c + 1, t + 1):
                print(f"lift is moving to floor {floor}")
                time.sleep(1)  
            c = t
        elif t < c:
            print(f"Moving down to floor {t}")
            for floor in range(c - 1, t - 1, -1):
                print(f"lift is moving to floor {floor}")
                time.sleep(1)
            c = t
        else:
            print("you are already on the requested floor.")

while True:
    print(f"Current floor: {c}")
    try:
        t = int(input("Enter the floor you want to go to (0-4): "))
        l(t)
    except ValueError:
        print("Invalid input. Please enter a number.")


