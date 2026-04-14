def parse_logs(file_path):
    try:
        with open(file_path, "r") as file:
            for line in file:

                if "Failed password" in line:
                    parts = line.split()

                    ip = "unknown"
                    if "from" in parts:
                        ip = parts[parts.index("from") + 1]

                    username = "unknown"
                    if "invalid user" in line:
                        username = parts[parts.index("user") + 1]
                    else:
                        username = parts[parts.index("for") + 1]

                    print(f"[ALERT] User: {username}, IP: {ip}")

    except FileNotFoundError:
        print("File not found")


if __name__ == "__main__":
    parse_logs("auth.log")
    
