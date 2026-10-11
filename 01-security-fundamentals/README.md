# Security Fundamentals

## Status
Completed learning exercise and controls mapping for a fictional small business.

## Objective
Document the core security principles that apply to a small business environment and explain how essential controls help protect confidentiality, integrity, and availability.

## Scenario
I assessed a fictional small business that stores employee records, customer contact data, and internal business files on company laptops and a shared Windows server. The business uses email, internet browsing, and a small office network, but it does not yet have a formal security baseline or user access review process.

## Security question
What security controls would best reduce the most common risks for this business while staying practical and cost-effective?

## Concepts applied
- CIA triad: confidentiality, integrity, availability
- Least privilege
- Defense in depth
- Asset value and risk prioritization
- Security control categories: preventive, detective, corrective, and recovery

## Findings and controls mapping

| Asset | Example risk | Security concern | Preventive control | Detective control | Recovery control |
|---|---|---|---|---|---|
| Employee laptops | Malware or phishing compromise | Confidentiality and integrity loss | Endpoint protection and user awareness training | Security alerts from antivirus and email filtering | Confirm backup restore and reimage infected systems |
| Customer records | Unauthorized access or disclosure | Privacy and regulatory risk | Role-based access control and encryption at rest | Access review reports and audit logs | Restore from secure backup and revoke compromised credentials |
| Email system | Phishing or business email compromise | Credential theft and fraud | MFA and phishing-resistant authentication | Email security alerts and mailbox activity monitoring | Disable compromised accounts and reset credentials |
| Shared server | Misconfiguration or unauthorized privilege escalation | Integrity and availability issues | Least privilege and hardening standards | Log review and change monitoring | Restore from validated backup and patch vulnerable services |
| Office network | Unpatched devices or lateral movement | Operational disruption | Network segmentation and patching schedule | IDS/IPS or firewall event review | Isolate affected segments and reapply baseline configuration |

## Analysis

The most important risk for this business is the combination of user access, weak visibility, and a lack of a formal patching or monitoring routine. If an employee account is compromised, the business could lose customer trust, expose private data, or allow malware to spread across the network. The controls above align with security fundamentals because they reduce exposure, improve detection, and support recovery without requiring a large enterprise security architecture.

## Recommendations

1. Enforce least privilege for all employee accounts and service accounts.
2. Require MFA on email and remote access.
3. Deploy endpoint protection and patching for all laptops and servers.
4. Back up key files and test restoration regularly.
5. Review security logs and access logs at least weekly.
6. Train staff on phishing recognition and safe handling of sensitive information.

## References

- National Institute of Standards and Technology (NIST) Cybersecurity Framework
- Google Cybersecurity Certificate course content on security controls and the CIA triad

## Lessons learned

This exercise reinforced that foundational security is not only about blocking attacks but also about reducing the impact when a failure happens. A small business may not need extensive enterprise tooling, but it does need simple, consistent controls that support confidentiality, integrity, and availability. I also learned that security recommendations are stronger when they are tied to specific assets and realistic risks instead of generic advice.
