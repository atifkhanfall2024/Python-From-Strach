# Create a set
nums = {1, 2, 3, 3, 4}
print(nums)  # {1, 2, 3, 4} → duplicates removed

# Add
nums.add(5)

# Remove
nums.remove(2)

# Check membership
print(3 in nums)  # True

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)  # Union → {1, 2, 3, 4, 5}
print(a & b)  # Intersection → {3}
print(a - b)  # Difference → {1, 2}
