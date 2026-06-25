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

# 3.Set , unordered, Unique values only , Notice duplicate is removed.

data = {1,2,3,4,5,6,1,2,55,67,67,8990}
data[0]=23
print(data)
print(type(data))
# data.append(2) AttributeError: 'set' object has no attribute 'append'

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


