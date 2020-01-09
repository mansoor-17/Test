# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods


name = 'Abc'
age = 27


# Concatenate

# print('Hello, my name is ' + name + ' and I am ' + str(age))   #str(age) is used because int cannot be concatinated to str

# String Formatting

# Arguments by position

# print('My name is {aaa} and I am {bbb}'.format(aaa=name, bbb=age))    #{name} and {age} are basically placeholders


# F-Strings (3.6+)


# print(f'Hello, my name is {name} and I am {age}')


# #------------------------------------------------------------------------------------------------------------------------------------


# # String Methods

s = 'helloworld'

# # Capitalize string
# print(s.capitalize())

# # Make all uppercase
# print(s.upper())

# # # Make all lower
# print(s.lower())

# # Swap case
# print(s.swapcase())

# Get length
# print(len(s))

# Replace
# print(s.replace('world', 'everyone'))

# Count
# sub = 'o'
# print(s.count(sub))

# Starts with
# print(s.startswith('ello'))

# # Ends with
# print(s.endswith('d'))

# Split into a list
# print(s.split())

# # Find position
print(s.find('r'))

# # Is all alphanumeric
print(s.isalnum())

# # Is all alphabetic
print(s.isalpha())

# # Is all numeric
print(s.isnumeric())

#------------------------------------------------------------------------------------------------------------------------------------