## Represent data store to keep track of passwords for different websites
Secret = {
    "thiswebsite.com": "password123",
    "thatwebsite.com": "securepassword"
}


## Function to validate that there is a password for a given website
def Exists(secretArray,char):
    # Check if the website exists in the secretArray
    # Loop index through the secretArray from [0] to [n]
    for i in secretArray:
        # If the website exists, return True
        if i == char:
            return True


    return False


if Exists(Secret,"thiswebsite.com"):
    print("Password exists in Secret")
else:
    print("Password does not exist Secret")