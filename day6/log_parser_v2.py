import sys
import os
import re


def extract_ip(line):
    match = re.search(r"\d+\.\d+\.\d+\.\d+", line)
    if match:
        return match.group()
    return "unknown"


def parse_logs(file_path):
    if not os.path.exists(file_path):
        print("File not found")
        return {}

    ip_count = {}

    with open(file_path, "r") as file:
        for line in file:

            if "Failed password" in line:
                ip = extract_ip(line)

                if ip != "unknown":
                    if ip in ip_count:
                        ip_count[ip] += 1
                    else:
                        ip_count[ip] = 1

    return ip_count


def show_top_attackers(ip_count):
    print("\nTop Attackers:")

    for ip, count in ip_count.items():
        print(f"{ip} → {count} attempts")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python log_parser_v2.py <logfile>")
    else:
        result = parse_logs(sys.argv[1])

        if result:
            show_top_attackers(result)
        else:
            print("No data to display")
    
