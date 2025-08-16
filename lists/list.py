fruitsArr = ["apple", "mango", "pinapple", "banana"]  # List of strings

# - Adding an element to the end
fruitsArr.append("orange")
# - Inserting an element at staring
fruitsArr.insert(0, "kiwi") 

# - remove last , first, second
fruitsArr.pop()         
fruitsArr.pop(0)      
fruitsArr.pop(1)       

# - slice list from index 1 to 2 , last does not include

new_fruits = fruitsArr[1:3]   

# print("New Fruits - ", new_fruits)

# - Iterate through the list

for fruit in fruitsArr:            
    print(f"Fruit - {fruit}")


# - To check if element is in list

if "apple" in fruitsArr:           
    print("Apple is in fruits")
else:
    print("Apple is not in fruits")


# print("Length of fruits Array/List - ", len(fruitsArr))

#  - Sorting list 

nums = [3, 1, 4, 2]
nums.sort()              # [1, 2, 3, 4
nums.reverse()           # [4, 3, 2, 1]

sorted_nums = sorted(nums)   

# - Join Array/List as a string

joinFruitsArr = ", ".join(fruitsArr) 

# - Spliting string into list

text = "apple,banana,cherry"

newTextArr = text.split(",")

# - Finding Index of Element

appleIndex = fruitsArr.index("apple")

# - Remove First occurence of an element

fruitsArr.remove("banana") 