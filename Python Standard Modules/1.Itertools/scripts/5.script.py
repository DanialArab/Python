# Chunk Data into Fixed Size Windows
# Split a list into non-overlapping windows of size n. 
# Use itertools.islice and yield each chunk as a list.

data = [1, 2, 3, 4, 5, 6, 7]
n = 3

# my solution without islice

# res = [] 
# for i in range(0, len(data), n):
#     res.append(data[i:i+n])
# print (res)

from itertools import islice

def chunker(data, n):
    it = iter(data)
    while True:
        chunk = list(islice(it, n))
        if not chunk:
            break
        yield chunk

for chunk in chunker(data, n):
    print(chunk)
print(chunker(data, n))