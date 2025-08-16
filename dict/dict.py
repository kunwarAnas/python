import json

userDetails  = {
    "name" : "alex",
    "age" : 20,
    "Address" : "xyz"
}

# for key , value in userDetails.items():
#     print(key, value)

if userDetails["name"] and userDetails["age"]:
    # print(f"Name {userDetails["name"]} , Age {userDetails['age']}")
    None
else:
    print("NOT FOUND")


# Merging Dictionaries

u1 = {"a": 1, "b": 2}
u2 = {"b": 3, "c": 4}
merged = {**u1, **u2}

# Parsing JSON config

config_str = '{"server": "localhost", "port": 8080}'
config = json.loads(config_str) 

print(config["server"])