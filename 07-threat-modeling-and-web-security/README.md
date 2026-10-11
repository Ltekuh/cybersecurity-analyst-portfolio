# Threat Modeling and Web Security

## Status
Completed threat-modeling exercise for a small web application.

## Objective
Identify the key threats for a fictional web application, map them to likely attack paths, and propose reasonable mitigations that reduce risk while maintaining usability.

## Application overview

The application is a small e-commerce system for a fictional online storefront. It has a public-facing website, an authentication system, a product catalog, a shopping cart, and a backend database that stores customer records, orders, and payment metadata. The application also exposes a support portal and admin dashboard for site staff.

## Assets and trust boundaries

| Asset / component | Why it matters | Trust boundary |
|---|---|---|
| Web storefront | Public facing and user access point | Internet to application boundary |
| User authentication | Protects customer accounts and order history | User to app boundary |
| Customer payment metadata | Sensitive business and user data | App to payment system boundary |
| Product catalog | Core business logic and customer experience | Application to database boundary |
| Admin panel | High-impact internal interface | Internal users to app boundary |

## Threats and mitigations

| Component or asset | Threat scenario | Potential impact | Existing or proposed control | Verification approach |
|---|---|---|---|---|
| Public web app | SQL injection through a product search field | Data exposure or application compromise | Parameterized queries, input validation, WAF rules | Run secure code review and test with sanitized input |
| Authentication system | Brute-force or credential stuffing attempts | Account takeover and fraud | Rate limiting, MFA, lockout policy | Review log volume and test login thresholds in a lab |
| Shopping cart | Cross-site scripting in product comments or forms | Session hijacking or account abuse | Output encoding, CSP headers, sanitization | Test form submission with known safe and unsafe inputs |
| Admin dashboard | Privilege escalation from a low-privilege user | Unauthorized access to orders and data | RBAC, least privilege, separate admin accounts | Review access matrix and test role permissions |
| Payment metadata | Insecure handling of customer data | Privacy violations and compliance issues | Encryption in transit and at rest, restricted access | Check config review and verify encryption settings |
| Session management | Session fixation or cookie theft | Account takeover | Secure cookies, timeout policies, token rotation | Inspect browser session settings and application logs |

## Threat analysis

The most important risks are tied to user input, authentication, and privilege boundaries. If the application accepts untrusted input without validation, attackers may exploit it to manipulate queries or inject malicious scripts. If admin permissions are not strictly separated, an attacker could move from a low-privilege account into a critical business function. These risks matter because they can lead to data exposure, fraud, or operational disruption without requiring advanced techniques.

## Recommendations

1. Enforce input validation and parameterized database queries.
2. Require MFA for customer and admin accounts.
3. Apply separate roles with least privilege for employees and support users.
4. Use secure cookie and session handling with timeouts.
5. Monitor authentication failures and privilege changes.
6. Validate that the application is using secure communication and limited access to sensitive data.

## Lessons learned

This exercise showed that threat modeling is most valuable when it starts with the application’s real trust boundaries and user roles. I learned that even a small web application can have major risks when data flow, authentication, and authorization are not clearly designed and reviewed. The most important takeaway is that effective security design reduces attack surface early, before code is deployed or exposed to real users.
