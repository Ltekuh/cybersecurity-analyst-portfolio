# Security Hardening

## Status
Completed baseline hardening checklist for a Linux lab system.

## Objective
Apply a basic hardening baseline to a Linux test system and verify the results with safe, repeatable checks. The goal is to reduce unnecessary exposure while preserving usability for a lab environment.

## Test environment

I used a Linux virtual machine or sandboxed lab environment that was explicitly designated for learning and testing. The system was not connected to production infrastructure, and all hardening steps were applied intentionally and verified afterward.

## Baseline reference

The hardening process follow general Linux security principles:

- remove unnecessary services
- restrict root and sudo access
- apply system updates
- enable logging and time synchronization
- define firewall rules for expected traffic only
- verify file permissions on sensitive files

## Hardening checklist

| Recommendation | Why it matters | Planned change | Verification command or check | Result | Trade-off |
|---|---|---|---|---|---|
| Apply system updates | Unpatched systems are vulnerable to known issues | Run package updates and reboot if required | `sudo apt update && sudo apt upgrade -y` | Updates completed successfully | Brief maintenance window needed |
| Remove unnecessary services | Extra services expand the attack surface | Disable unused daemons and confirm they are not running | `systemctl list-units --type=service --state=running` | Only required services remained active | Some features may be unavailable if misidentified |
| Restrict root access | Direct root use increases privilege risk | Require sudo for administrative actions and review sudoers | `sudo -l` and `sudo whoami` | Administrative access is governed by sudo | Users need a clear process for elevated tasks |
| Harden file permissions | Sensitive logs and configuration files should not be broadly writable | Restrict ownership and permissions on `/etc/passwd`, `/etc/shadow`, and logs | `ls -l /etc/passwd /etc/shadow` | Sensitive files remained protected | Requires care when updating system files |
| Configure firewall | The system should only allow required networking | Allow SSH access only from the lab subnet | `sudo ufw status` | Only approved traffic was permitted | Some services may be blocked if not documented |
| Enable logging and review | Logs help detect misuse or unauthorized changes | Ensure syslog or journald is configured and rotating | `journalctl -n 20` and log directory checks | Recent events were available and readable | More log volume requires periodic review |

## Verification summary

The hardening steps above were verified by checking the active services, firewall status, user authorization, and sensitive file permissions. The system remains functional for a test environment while reducing default exposure and limiting unnecessary access.

## Operational notes

- Services should be reviewed regularly because software changes can reintroduce risk.
- Firewall and access rules should be documented so they remain understandable to the operator.
- Logging is only useful if someone reviews it regularly; otherwise it becomes a background artifact.

## Lessons learned

This project reinforced that hardening is not a one-time task; it is a recurring discipline. I learned that the most effective baseline controls are simple, measurable, and easy to verify. A secure system is not necessarily a locked-down system; it is a system with a clear understanding of which services, users, and network paths are intentionally allowed.
