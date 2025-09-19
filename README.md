# CodeAlpha_Task3-SecureCodingReview

# 🔒 Task 3 – Secure Coding Review

## 📌 Overview
This task demonstrates a **secure coding review** of a Python login system.  
We identify vulnerabilities in the insecure version and provide a **secure implementation** aligned with OWASP best practices.

## 🛠️ Features
- Review of insecure login system
- Identification of vulnerabilities:
  - Hardcoded credentials
  - Plaintext password comparison
  - Weak authentication controls
- Recommendations for secure coding
- Improved secure login system:
  - Password hashing with SHA-256
  - Environment variable for secret storage
  - Defensive programming practices
- Full professional report (`SecureCodingReport.pdf`)

## 📂 Project Structure


## ▶️ How to Run Secure Code
1. Set environment variable for admin password:
   - Linux/Mac:
     ```bash
     export ADMIN_PASSWORD="StrongPassword123"
     ```
   - Windows PowerShell:
     ```powershell
     $env:ADMIN_PASSWORD="StrongPassword123"
     ```
2. Run the secure script:
   ```bash
   python secure_logincode.py
