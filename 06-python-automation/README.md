# Python Automation for Security Tasks

## Status
Completed beginner-friendly automation exercise using a fake access log and a Python script.

## Objective
Create a small script that checks whether IP addresses are valid, reviews a sample log, and identifies repeated failed logins that may indicate suspicious activity.

## Tools used

- Python 3.10+
- Standard library modules: `ipaddress`, `collections`, and `re`
- A sanitized sample log file created for learning and testing

## Project summary

I built a script that reads a small access log, validates the IP addresses found in it, counts event types, and highlights repeated failed login attempts from the same source. This is a practical example of basic automation in a security context because it makes repeated review faster and easier to standardize.

## Files in this folder

- `log_analyzer.py` - the Python script
- `sample_auth.log` - sanitized sample log input

## How to run the script

```bash
python log_analyzer.py sample_auth.log
```

## Sample input

```text
2026-06-19 08:15:11 INFO User alice logged in from 10.0.0.12
2026-06-19 08:18:34 WARNING Failed login for user bob from 10.0.0.12
2026-06-19 08:19:02 WARNING Failed login for user bob from 10.0.0.12
2026-06-19 08:20:11 WARNING Failed login for user bob from 10.0.0.12
2026-06-19 08:21:54 INFO User bob logged in from 10.0.0.12
2026-06-19 08:22:05 WARNING Failed login for user carol from 192.168.1.40
2026-06-19 08:22:38 ERROR Invalid IP address in request: 999.999.999.999
2026-06-19 08:23:00 INFO User carol logged in from 192.168.1.40
2026-06-19 08:24:31 WARNING Failed login for user dave from 172.16.0.44
2026-06-19 08:25:13 WARNING Failed login for user dave from 172.16.0.44
2026-06-19 08:26:02 WARNING Failed login for user dave from 172.16.0.44
```

## Expected output

```text
Security log summary
====================
Total lines processed: 11
Valid IPs found: 10
Invalid IPs found: 1
Failed login attempts by IP:
  10.0.0.12: 3
  172.16.0.44: 3
  192.168.1.40: 1

Possible suspicious activity:
  10.0.0.12 - 3 failed login attempts
  172.16.0.44 - 3 failed login attempts
  192.168.1.40 - 1 failed login attempts
```

## What the script does

- Reads a log file line by line
- Extracts IP addresses from log messages
- Validates them with Python's `ipaddress` module
- Counts failed attempts by source IP
- Prints a simple summary of suspicious repeated activity

## What the script does not do

- It does not block traffic or interact with a live system.
- It does not determine intent or maliciousness with certainty.
- It does not replace full log analysis or incident response workflow.

## Limitations and improvements

This script is intentionally small and is best suited for learning and basic triage. In a real environment, I would also add timestamp parsing, a stricter alert threshold, and optional output to CSV or JSON for easier reporting. I would also want richer context such as user agent, source port, and associated system logs before deciding whether an event is suspicious.

## Lessons learned

This project showed me how a simple script can make repetitive security tasks more manageable and easier to understand. I learned that automation is most useful when it reduces manual review, standardizes evidence collection, and creates a clear summary for future investigation. It also reinforced the importance of separating a technical finding from a security conclusion.
