import time

# user database and failure tracker
users = {"admin": "1234", "user": "abcd"}
fails = {}

# countdown timer for lock period
def cd(t):
    while t:
        print(f"\rRetry in {t} seconds", end="")
        time.sleep(1)
        t -= 1
    print("\nYou can try again.\n")

# main loop (menu)
while True:
    print("1. Login\n2. Exit")
    c = input("Choose option: ")

    if c == "2":  # exit program
        print("Exiting system...")
        break

    if c != "1":  # invalid menu choice
        print("Invalid choice\n")
        continue

    u = input("Enter username: ")
    if u not in users:  # user check
        print("User not found\n")
        continue

    fails.setdefault(u, 0)  # initialize failure count

    # password attempts (max 3)
    for i in range(1, 4):
        if input("Enter password: ") == users[u]:
            print("Login successful\n")
            fails[u] = 0  # reset on success
            break
        print(f"Incorrect password ({i}/3)")
    else:
        # lock after 3 failures
        fails[u] += 1
        lock = 5 * fails[u]  # increasing lock time
        print(f"\nToo many attempts. Account locked for {lock} seconds.")
        cd(lock)      
