userDetails = {
    "name": "Anas",
    "Address" : "Xyz"
}

userDetails2 = {
    "name": "Alex",
    "Address": "abc"
}

def processUser(*args):
    details = args
    userMapping = {
        "user1" : details[0],
        "user2" : details[1]
    }
    return userMapping



data = processUser(userDetails, userDetails2)

print("data - " , data)