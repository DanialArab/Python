fruits = ["apple", "banana", "cherry"]
prices = [0.99, 0.59, 2.99]
# Use zip() to make a dictionary mapping fruit to price.

my_dict = {}
for f, p in zip(fruits, prices):
    my_dict[f] = p

print (my_dict)

print(f"better and more concise way: {dict(zip(fruits, prices))}")