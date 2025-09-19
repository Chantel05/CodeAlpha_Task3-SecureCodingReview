# CodeAlpha_Task3-SecureCodingReview

# Task 3 – Secure Coding Review

## Overview
This task demonstrates a secure coding review of a Python login system.  
We identify vulnerabilities in the insecure version and provide a secure implementation following OWASP standards.

## Deliverables
- `insecure_login.py` → Original vulnerable code
- `secure_login.py` → Secure, improved version
- `SecureCodingReport.pdf` → Full professional audit report

## How to Run
1. Set environment variable for admin password:
   - On Linux/Mac: `export ADMIN_PASSWORD="StrongPassword123"`
   - On Windows (PowerShell): `$env:ADMIN_PASSWORD="StrongPassword123"`
2. Run the secure script:
   ```bash
   python secure_login.py
