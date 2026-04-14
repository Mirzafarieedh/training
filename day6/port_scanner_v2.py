import socket

target = "127.0.0.1"

print(f"Scanning {target}...\n")

for port in range(7900, 8100):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    result = s.connect_ex((target, port))

    if result == 0:
        try:
            banner = s.recv(1024).decode().strip()
        except:
            banner = "No banner"

        print(f"[OPEN] Port {port} → {banner}")

    s.close()