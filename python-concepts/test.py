# Create a set
myset = {9,1,2,2,1, 2, 3}

# 1. Add a single element
myset.add(4)  
print(myset)   # {1, 2, 3, 4}

# 2. Add multiple elements (from another set, list, or tuple)
myset.update([5, 6, 7])  
print(myset)   # {1, 2, 3, 4, 5, 6, 7}

# 3. Remove an element (error if not found)
myset.remove(2)  
print(myset)   # {1, 3, 4, 5, 6, 7}

# 4. Discard an element (no error if not found)
myset.discard(9)   # does nothing since 10 isn’t in the set

# 5. Pop an element (removes a random item)
removed = myset.pop()
print("Removed:", removed)
print(myset)
