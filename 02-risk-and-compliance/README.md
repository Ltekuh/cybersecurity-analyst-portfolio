# Risk and Compliance

## Status
Completed small-business risk assessment based on a fictional scenario and a basic control review.

## Objective
Identify the most important security risks for a small business and prioritize them based on the likelihood of occurrence and impact to confidentiality, integrity, and availability.

## Scope and assumptions

This assessment covers a fictional retail business with a small office network, employee laptops, customer records, email, and a wireless router. I assume the business stores customer contact information, uses local file sharing, and relies on internet access for business operations. The risk ratings below are estimates for the scenario and should not be treated as measured historical facts.

## Risk register

| Risk ID | Asset / area | Threat | Likelihood | Impact | Risk rating | Recommended control | Residual risk |
|---|---|---|---|---|---|---|---|
| R-01 | Employee laptops | Malware via phishing email | Medium | High | High | Email filtering, MFA, endpoint protection, employee awareness training | Medium if users continue to click unknown links |
| R-02 | Customer records | Unauthorized access to databases or shared folders | Medium | High | High | RBAC, encryption, access review, least privilege | Medium if controls are not enforced consistently |
| R-03 | Router / office network | Weak default configuration or misconfigured wireless access | Medium | Medium | Medium | Change default credentials, update firmware, disable unused services | Low if periodic review is maintained |
| R-04 | Shared server | Insufficient patching and account monitoring | Medium | High | High | Patch management, privileged account review, logging | Medium if patching is delayed |
| R-05 | Email account | Business email compromise or credential theft | High | High | High | MFA, password policies, mailbox monitoring | Medium if users do not report suspicious requests |
| R-06 | Backup systems | Failure to recover from ransomware or system loss | Low | High | Medium | Test restoration, store backups separately, monitor backup success | Low if backup validation is ongoing |

## Risk prioritization

I prioritized the risks by combining likelihood and impact to focus on the controls most likely to reduce harm quickly. The highest-priority risks are tied to phishing, customer-data exposure, and weak account management because they can quickly cause confidentiality loss and financial damage. Lower-priority items, such as backup continuity, still matter, but they are easier to address once the direct access and resilience controls are in place.

## Recommended controls

1. Require MFA for email and administrative access.
2. Enforce least privilege for employees and departments.
3. Implement patching and endpoint protection across laptops and servers.
4. Restrict wireless access and update routers with secure settings.
5. Review access logs and change logs weekly.
6. Run periodic backup tests and document restoration steps.

## Residual risk notes

Some residual risk remains because user behavior and configuration drift can introduce vulnerabilities even after controls are implemented. For example, a user may still fall for a convincing phishing email, or an unapproved application may create a data exposure issue. This is why detective controls, alert review, and routine validation remain important.

## Framework and guidance

This assessment is aligned with general security risk principles and follows a practical approach consistent with the NIST Cybersecurity Framework, especially the Identify, Protect, Detect, and Recover functions. The ratings are scenario-based estimates rather than measured risk metrics.

## Lessons learned

This exercise reinforced that risk assessment is about more than listing threats; it is about deciding which controls most reduce harm given the business context. I learned that small environments often need a layered, low-complexity control set that balances technical protections with staff awareness and operational discipline. The final takeaway is that a business should prioritize controls that reduce the chance of high-impact events and improve recovery when incidents happen.
