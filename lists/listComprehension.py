logs = ["OK user1", "FAIL user2", "OK user3", "FAIL user4"]

# list comprehensions / Filtering 
okLogs = [line  for line in logs if "OK" in line] # [item for item in list if condition]

logs = ["User 192.168.1.1 connected", "User 10.0.0.2 disconnected"]

# list comprehensions / Mapping 
ipInLogs = [line.split(" ")[1] for line in logs] # [expr for item in list]