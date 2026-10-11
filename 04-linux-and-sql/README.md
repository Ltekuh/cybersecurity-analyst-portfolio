# Linux and SQL Security Practice

## Status
Completed Linux and SQL safety exercises using fictional data and a controlled lab environment.

## Objective
Practice common Linux security commands and SQL queries that help answer questions about permissions, access events, and abnormal activity patterns while avoiding real-world personal data.

## Linux practice

### Example 1: Review file permissions

Command:

```bash
ls -l /tmp/security-lab/
```

Sample output:

```text
-rw-r--r-- 1 alice staff  2048 Jun 18 10:42 notes.txt
-rwxr-x--- 1 bob   analysts  4096 Jun 18 10:45 script.sh
-rw------- 1 root root  1024 Jun 18 10:47 audit.log
```

### What this shows

- `notes.txt` is readable by the owner and group, and everyone else can read it.
- `script.sh` is executable by the owner, and group members have read/write/execute access.
- `audit.log` is readable only by the root user, which is a strong example of least privilege for sensitive logs.

### Security lesson

The goal is to prevent broad access to files that contain sensitive information or operational data. Overly permissive permissions are a common risk because they allow unauthorized modification or leakage.

### Example 2: Review processes and users

Command:

```bash
ps -ef | grep python
who
```

Sample output:

```text
root     1421  1  0 Jun18 ?  00:00:00 python3 /opt/monitor.py
alice    1831  1  0 Jun18 pts/0  00:00:00 bash
bob      2014  1  0 Jun18 pts/1  00:00:00 bash
```

### What this shows

This helps confirm which users are active and whether unusual services are running. For example, a Python process running as root may need review if it is not part of a known monitoring service.

## SQL practice

### Fictional access-events table

```sql
SELECT event_id, username, action, event_time
FROM access_events
WHERE action = 'failed_login'
ORDER BY event_time DESC
LIMIT 10;
```

Sample output:

```text
event_id | username | action         | event_time
---------+----------+----------------+---------------------
101      | bob      | failed_login   | 2026-06-18 10:41:00
102      | alice    | failed_login   | 2026-06-18 10:42:10
103      | admin    | failed_login   | 2026-06-18 10:43:30
104      | bob      | failed_login   | 2026-06-18 10:43:55
```

### What this shows

This query helps identify repeated failed login attempts. It is useful for targeting a potential brute-force pattern, but it does not prove that an attacker successfully compromised a system.

### Example with filtering and range checks

```sql
SELECT username, COUNT(*) AS failed_attempts
FROM access_events
WHERE action = 'failed_login'
  AND event_time BETWEEN '2026-06-18 10:00:00' AND '2026-06-18 11:00:00'
GROUP BY username
ORDER BY failed_attempts DESC;
```

Sample output:

```text
username | failed_attempts
---------+----------------
bob      | 6
admin    | 4
alice    | 2
```

### Security lessons from SQL

- `WHERE` filters the relevant events.
- `ORDER BY` helps prioritize suspicious behavior.
- `GROUP BY` supports trend analysis.
- This query highlights repeated failed attempts, but it cannot prove a malicious actor without surrounding logs and system context.

## Recommendations

1. Use least-privilege permissions on files and directories.
2. Review file ownership and access controls regularly.
3. Investigate repeated failed logins and lock accounts when thresholds are exceeded.
4. Keep audit logs and preserve evidence in a secure location.

## Lessons learned

This exercise showed that Linux and SQL skills are not just about syntax; they are about answering security questions clearly and responsibly. I learned how access controls and log review can point to risk before an incident becomes severe. The main takeaway is that security data is most useful when it is analyzed with context, scope, and a clear distinction between evidence and inference.
