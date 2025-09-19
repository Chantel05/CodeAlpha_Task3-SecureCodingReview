
import hashlib
import os

# Store password securely in environment variable
# Example: export ADMIN_PASSWORD="StrongPassword123"
stored_hash = hashlib.sha256(os.environ.get("ADMIN_PASSWORD", "default").encode()).hexdigest()

username = input("Enter username: ")
password = input("Enter password: ")

# Hash user input before comparing
hashed_pw = hashlib.sha256(password.encode()).hexdigest()

if username == "admin" and hashed_pw == stored_hash:
    print("Login successful ✅")
else:
    print("Invalid credentials ❌")
