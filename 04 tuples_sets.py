# # A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# # Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')
# print(fruits,type(fruits))

# # Using a constructor
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# print(fruits2)
# # Single value needs trailing comma

# fruits2 = ('Apples')      #the type() returns it as <class 'str'>
# print(fruits2,type(fruits2))
# fruits2 = ('Apples',)       #the type() returns it as <class 'tuple'>
# print(fruits2,type(fruits2))
# # Get value
# print(fruits[1])        #to get a value is same as a list

# # Can't change value
fruits[0] = 'Pears'

# # Delete tuple
# del fruits2

# # Get length
# print(len(fruits))

#-------------------------------------------------------------------------------------------------------------------------------------


# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
# fruits_set = {'Apples', 'Oranges', 'Mango'}

# # Check if in set
# # print('Apples' in fruits_set)

# # # Add to set
# fruits_set.add('Grape')
# # print(fruits_set)

# # # Remove from set
# fruits_set.remove('Grape')
# # print(fruits_set)

# # # Add duplicate
# # fruits_set.add('Apples')
# print(fruits_set)

# # # Clear set
# # fruits_set.clear()

# # # Delete
# del fruits_set

# # print(fruits_set)
