import time

# ==============================
# 1. NUMERIC PIN BRUTE FORCE
# ==============================

def crack_pin(target, digits=5, log_interval=10000):
    start = time.time()
    attempts = 0

    max_range = 10 ** digits

    for i in range(max_range):
        attempts += 1
        guess = str(i).zfill(digits)

        # Controlled logging
        if attempts % log_interval == 0:
            print(f"Tried {attempts} guesses...")

        if guess == target:
            end = time.time()
            print("\n[PIN CRACKED]")
            print("Target:", target)
            print("Attempts:", attempts)
            print("Time:", round(end - start, 4), "seconds")
            return

    print("Failed to crack PIN")


# ==============================
# 2. RECURSIVE PASSWORD BRUTE FORCE
# ==============================

def brute_force(chars, target, log_interval=10000):
    start = time.time()
    attempts = [0]  # use list to mutate inside recursion

    def helper(current):
        # Base case
        if len(current) == len(target):
            attempts[0] += 1

            if attempts[0] % log_interval == 0:
                print(f"Tried {attempts[0]} guesses...")

            if current == target:
                end = time.time()
                print("\n[PASSWORD CRACKED]")
                print("Target:", target)
                print("Attempts:", attempts[0])
                print("Time:", round(end - start, 4), "seconds")
                return True
            return False

        # Recursive generation
        for ch in chars:
            if helper(current + ch):
                return True

        return False

    helper("")


# ==============================
# 3. RUN TESTS
# ==============================

if __name__ == "__main__":

    print("=== NUMERIC PIN TEST ===")
    crack_pin("04237", digits=5)

    print("\n=== PASSWORD TEST ===")
    brute_force("abc123", "a1c")