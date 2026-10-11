import re
from collections import defaultdict
from ipaddress import ip_address
from pathlib import Path
import sys

LINE_PATTERN = re.compile(r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+(INFO|WARNING|ERROR)\s+(.+)$")
IP_PATTERN = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")


def is_valid_ip(value: str) -> bool:
    try:
        ip_address(value)
        return True
    except ValueError:
        return False


def parse_log(file_path: str):
    total_lines = 0
    valid_ips = 0
    invalid_ips = 0
    failed_attempts = defaultdict(int)
    seen_ips = set()

    path = Path(file_path)
    if not path.exists():
        print(f"Error: file not found: {file_path}")
        sys.exit(1)

    with path.open("r", encoding="utf-8") as file:
        for line in file:
            total_lines += 1
            match = LINE_PATTERN.match(line.strip())
            if not match:
                continue

            timestamp, level, message = match.groups()
            ips = IP_PATTERN.findall(message)

            for ip in ips:
                if is_valid_ip(ip):
                    valid_ips += 1
                    seen_ips.add(ip)
                    if "Failed login" in message:
                        failed_attempts[ip] += 1
                else:
                    invalid_ips += 1

    suspicious = [
        (ip, count) for ip, count in sorted(failed_attempts.items(), key=lambda item: (-item[1], item[0]))
        if count > 0
    ]

    print("Security log summary")
    print("====================")
    print(f"Total lines processed: {total_lines}")
    print(f"Valid IPs found: {valid_ips}")
    print(f"Invalid IPs found: {invalid_ips}")
    print("Failed login attempts by IP:")
    if suspicious:
        for ip, count in suspicious:
            print(f"  {ip}: {count}")
    else:
        print("  No failed login attempts detected.")

    if suspicious:
        print("\nPossible suspicious activity:")
        for ip, count in suspicious:
            print(f"  {ip} - {count} failed login attempts")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python log_analyzer.py <logfile>")
        sys.exit(1)

    parse_log(sys.argv[1])
