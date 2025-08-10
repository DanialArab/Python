
# Use zip() to combine them into a list of tuples:

def combiner(l1, l2):
    res = [] 
    for i, j in zip(l1, l2):
        res.append((i,j))
    return res

def better_com(l1, l2):
    return list(zip(l1, l2))

def main():
    names = ["Alice", "Bob", "Charlie"]
    scores = [85, 92, 78]
    print(better_com(names, scores))


if __name__ == '__main__':
    main()