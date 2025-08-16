# 1. Basic Function

def greet(name):
    return f"Hello {name}" # String interpolation

res = greet('Anas')

# 2. Default Parameters

def greet(name="Guest"):
    return f"Hello, {name}"

# 3. Multiple Return Values / Destructuring List/tuple

def get_user():
    return "Anas", "Admin"   # returns tuple

name, role = get_user()
print(name, role)  

# 4. Anonymous Functions (Lambdas)

square = lambda x: x * x
square(5)

# Functions with Variable Arguments

def sum_numbers(*nums):   # *nums = tuple of args
    return sum(nums)

sum_numbers(1, 2, 3, 4)  # 10
