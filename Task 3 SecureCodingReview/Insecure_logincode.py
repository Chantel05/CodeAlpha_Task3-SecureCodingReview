
# Insecure login code (example)
username = input("Enter username: ")
password = input("Enter password: ")

# Hardcoded credentials (bad practice!)
if username == "admin" and password == "12345":
    print("Login successful")
else:
    print("Invalid credentials")
