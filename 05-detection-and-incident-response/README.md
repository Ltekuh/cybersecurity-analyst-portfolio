# Detection and Incident Response

## Status
Completed SOC-style alert triage and incident documentation using fictional log evidence.

## Objective
Assess a suspicious alert, support the conclusion with evidence, and document the likely response steps in a professional incident-handling format.

## Scenario
A training environment generated an alert for repeated failed login attempts followed by a successful login from an unfamiliar endpoint. I reviewed the sequence of events and documented whether the alert was a true positive, false positive, or inconclusive based on the evidence available.

## Alert summary

**Alert:** Multiple failed logins followed by a successful login after a password-reset workflow.  
**Severity rationale:** Medium to high because the activity suggests potential unauthorized access to a user account, especially if the account has privileged access or sensitive data.

## Timeline of observed events

| Time | Event | Observed fact |
|---|---|---|
| 08:15 | Login attempts begin | Several failed user logins from an unusual IP range |
| 08:18 | Password reset or credential change | Account activity shows a reset occurring shortly after the failed attempts |
| 08:22 | Successful login | A successful sign-in occurs from a new geolocation or unfamiliar endpoint |
| 08:25 | Privileged action | User attempted to access sensitive files or administrative portals |
| 08:30 | Security team review | Alert triage begins and access is investigated |

## Observable indicators

- Multiple failed authentication events within a short time window
- Successful login from an unfamiliar device or IP segment
- Follow-on activity suggesting account misuse or reconnaissance
- Event sequence that aligns more with credential abuse than a normal user error pattern

## Evidence supporting the alert

- Failed logins happened repeatedly before the account was successfully accessed.
- The successful login came from an unfamiliar location or device fingerprint.
- The user immediately accessed sensitive systems or records after the successful sign-in.
- The timeline matches a common pattern of credential stuffing, password spray, or compromised credentials.

## Evidence contradicting or limiting the alert

- The account owner may have been traveling or working from a different location.
- A legitimate user may have been using a VPN or shared device.
- The environment lacks complete endpoint telemetry to confirm the actor identity.
- Without a full login history, it is impossible to say with certainty whether the access was malicious or user-driven.

## Conclusion

The alert appears to be a likely true positive, but it is not conclusively proven without additional evidence. The combination of repeated failed logins and a successful sign-in from an unfamiliar endpoint is strong enough to justify investigation and containment.

## Response actions

### Containment

- Disable or lock the suspicious account.
- Reset the password and revoke active sessions.
- Block the offending IP range if the source is confirmed malicious.

### Eradication

- Review for unauthorized changes or file access.
- Search for persistence mechanisms or abnormal scheduled tasks.
- Validate whether other accounts were targeted in the same pattern.

### Recovery

- Restore the account only after verification that no unauthorized actions remain.
- Require MFA on the account and confirm user identity.
- Document lessons learned and improve detection thresholds.

### Follow-up

- Add detection for repeated failed logins followed by successful sign-ins.
- Review whether a password reset workflow is creating exploitable gaps.
- Ensure staff know how to report suspicious account events quickly.

## References

- NIST guidance for incident response and log analysis
- Google Cybersecurity Certificate coursework on detection and response
- Repository template: `../templates/incident-report.md`

## Lessons learned

This exercise reinforced that security alerts are strongest when they are assessed as a sequence of evidence rather than a single anomaly. I learned to separate what is observed from what is inferred, and to document both the supporting evidence and the limits of the available data. That type of disciplined reporting is essential in a SOC environment, where clear actions and accurate conclusions matter more than guessing at intent.
