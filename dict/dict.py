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

# get key or values as array/list

user = {"name": "Alice", "age": 25}
user.keys()     # dict_keys(['name', 'age'])
user.values() # dict_keys(['Alice', '25'])
list(user.keys()) # ['name', 'age']


# .get(key, default) → Safe access

user.get("name", "Unknown")  # Alice
user["city"] # Throws error as no city key 
user.get("city", "Unknown")  # Unknown

# Merging Dictionaries

u1 = {"a": 1, "b": 2}
u2 = {"b": 3, "c": 4}
merged = {**u1, **u2}

# Parsing JSON config

config_str = '{"server": "localhost", "port": 8080}'
config = json.loads(config_str) 