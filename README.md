# Cybersecurity Analyst Portfolio

This repository documents my learning and hands-on practice in cybersecurity. It brings together coursework, lab exercises, analysis write-ups, and beginner-friendly projects completed while working toward entry-level Cybersecurity Analyst and Security Operations Center (SOC) Analyst roles.

The examples are educational and use fictional scenarios, sanitized data, or authorized lab environments. They demonstrate what I practiced; they are not claims of professional experience.

## Portfolio contents

| Section | Overview |
|---|---|
| [Certificate and Skills](00-certificate-and-skills/README.md) | Google Cybersecurity Certificate coursework and skills practiced |
| [Security Fundamentals](01-security-fundamentals/README.md) | Core security principles, controls, and a small-business scenario |
| [Risk and Compliance](02-risk-and-compliance/README.md) | Scenario-based risk assessment, risk register, and mitigation planning |
| [Network Security](03-network-security/README.md) | Wireshark packet-analysis lab and traffic observations |
| [Linux and SQL](04-linux-and-sql/README.md) | Linux permissions and SQL-based review of fictional access events |
| [Detection and Incident Response](05-detection-and-incident-response/README.md) | SOC-style alert triage and incident documentation |
| [Python Automation](06-python-automation/README.md) | A Python script for reviewing a sample authentication log |
| [Threat Modeling and Web Security](07-threat-modeling-and-web-security/README.md) | Threat scenarios and mitigations for a fictional web application |
| [Security Hardening](08-security-hardening/README.md) | A baseline hardening checklist for a Linux lab system |
| [Templates](templates/README.md) | Reusable templates for lab notes, incident reports, and risk assessments |

## Getting started

Browse the sections above to explore each exercise. Project write-ups describe their objectives, methods, observations, limitations, and recommendations.

To run the sample log-analysis script, install Python 3.10 or later and run this command from the repository root:

```powershell
python .\06-python-automation\log_analyzer.py .\06-python-automation\sample_auth.log
```

The script uses Python's standard library and does not require additional packages. See the [Python Automation project](06-python-automation/README.md) for details and limitations.

## Skills practiced

- Security fundamentals, risk assessment, and control mapping
- Network traffic and packet analysis with Wireshark
- Linux command-line use and file permissions
- SQL queries for reviewing fictional access events
- Python basics for simple security-related automation
- Alert triage, incident documentation, and evidence-based reporting
- Threat modeling, application security, and security hardening

These skills were practiced through coursework and simulated exercises. Findings distinguish observable evidence from assumptions and note relevant limitations.

## Certificate

**Google Cybersecurity Certificate — completed**

- [Credential](https://coursera.org/share/df43041e6c50ae8d4b0e68ec934fbf1c)
- Completion date: October 9, 2026
- Coursework details and module credentials: [Certificate and Skills](00-certificate-and-skills/README.md)

## Responsible use

- Use tools and techniques only in authorized labs, systems, and exercises.
- Do not publish passwords, tokens, personal information, confidential course materials, or private network captures.
- Use fictional or sanitized examples in public documentation.
- Do not present simulated activity as a real incident.
- Support conclusions with evidence, state uncertainty, and document limitations.

---

*Portfolio status: active; coursework, lab notes, and projects are added as learning progresses.*
