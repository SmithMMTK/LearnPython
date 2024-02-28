# Define a dictionary to contain website and password pairs
Secret = {
    "thiswebsite.com": "password123",
    "thatwebsite.com": "securepassword"
}

# Accessing the password for a specific website
website = "thiswebsite.com"
password = Secret.get(website)


if password is not None:
    print(f"The password for {website} is: {password}")
else:
    print(f"No password found for {website}")


