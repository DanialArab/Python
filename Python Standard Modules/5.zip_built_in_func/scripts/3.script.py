# Unzip (reverse a zip) 
# Use zip() to separate names and ages into two tuples.

pairs = [("Tom", 20), ("Jerry", 18), ("Spike", 25)]
names, ages = zip(*pairs)
print (names)
print (ages )

# The * here is argument unpacking.

# Without the *, zip(pairs) would treat the whole list as a single item (not useful).

# With *pairs, it unpacks the list into separate arguments to zip()

