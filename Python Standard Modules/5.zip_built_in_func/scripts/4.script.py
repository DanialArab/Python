# Summation of corresponding list elements
# Use zip() to add corresponding elements together.


list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

print([i + j + k for i, j, k in zip(list1, list2, list3)])