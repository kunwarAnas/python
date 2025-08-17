# Creating a Set

nums = {1, 2, 3, 3, 2}  # {1, 2, 3}

# Adding Elements

nums.add(4) # {1, 2, 3, 4}

# Removing Elements

nums.remove(2)   # removes 2, error if not found
nums.discard(10) # removes if exists, no error if not


# Checking Membership

3 in nums  # True
5 in nums  # False

# Set Operations

a = {1, 2, 3}
b = {3, 4, 5}
a | b # UNION {1, 2, 3, 4, 5}
a & b # INTERSECTION{3}
a - b # DIFFRENCE # {1, 2}
a ^ b # Symmetric Difference (elements in either set but not both) {1, 2, 4, 5}