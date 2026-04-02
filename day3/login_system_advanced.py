import time

# =========================
# User Database
# =========================
users = {
    "admin": "1234",
    "user": "abcd"
}

# Track failed attempts globally
failed_attempts = {}

# =========================
# Countdown Function
# =========================
def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"\rRetry in {i} seconds", end="")
        time.sleep(1)
    print("\nYou can try again.\n")


# =========================
# Login Function
# =========================
def login_system():
    max_attempts = 3
    attempts = 0

    username = input("Enter username: ")

    if username not in users:
        print("User not found\n")
        return

    # Initialize failed attempts
    if username not in failed_attempts:
        failed_attempts[username] = 0

    while attempts < max_attempts:
        password = input("Enter password: ")
        attempts += 1

        if password == users[username]:
            print("Login successful\n")

            # Reset failed attempts on success
            failed_attempts[username] = 0
            return
        else:
            print(f"Incorrect password ({attempts}/{max_attempts})")

    # Increase failure count
    failed_attempts[username] += 1

    # Dynamic lock time (grows each failure)
    lock_time = 5 * failed_attempts[username]

    print(f"\nToo many attempts. Account locked for {lock_time} seconds.")
    countdown(lock_time)


# =========================
# Main Menu
# =========================
def main():
    while True:
        print("1. Login")
        print("2. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            login_system()
        elif choice == "2":
            print("Exiting system...")
            break
        else:
            print("Invalid choice\n")


# Run program
main()        