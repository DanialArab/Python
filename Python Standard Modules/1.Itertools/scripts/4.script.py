# Filter Elements Using a Mask

# Given a list of values and a list of binary flags (1 or 0), 
# return the values where the flag is 1 using itertools.compress

data = ['apple', 'banana', 'cherry', 'date']
flags = [1, 0, 1, 0]

# solution without compress 
# res = [] 
# for value, flag in zip(data, flags):
#     if flag == 1:
#         res.append(value)
# print (res)

from itertools import compress 

res = list(compress(data, flags))
print (res)
