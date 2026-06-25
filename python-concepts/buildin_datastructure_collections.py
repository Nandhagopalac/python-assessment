# 1.List can be changed - mutable , Ordered , duplicates allowed

fruits = ['mango','apple','mango']
print(fruits)
print(type(fruits))
fruits.append('banana')
print(fruits)

# 2.Touple cannot be changed the Order, duplicates allowed
coordinates = (10,20,33,345,44,33)
print(coordinates)
# coordinates.append(333) ttributeError: 'tuple' object has no attribute 'append'
# print(coordinates)

# Create a tuple of coordinates
coordinates = (10.5, 20.7)

# Access elements
print("X:", coordinates[0])   # 10.5
print("Y:", coordinates[1])   # 20.7

# Iterate through tuple
for value in coordinates:
    print(value)

# Count and index
numbers = (1, 2, 3, 2, 2)
print(numbers.count(2))   # 3 times
print(numbers.index(3))   # position of 3 is index 2


# 3.Set , unordered, Unique values only , Notice duplicate is removed.

data = {1,2,3,4,5,6,1,2,55,67,67,8990}
data[0]=23
print(data)
print(type(data))
# data.append(2) AttributeError: 'set' object has no attribute 'append'

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

# 4.dict, Stores data as key-value pairs
employees = {
    'name':'nandha',
    'age':32,
    'sal':2345.67,
    'is_active': True
}
print(type(employees))
employees['name']='gopal'
print(employees)
# 5 None type
data_none = None
print(data_none)
type(data_none)


