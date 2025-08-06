# Find Most Common Consecutive Word Pairs

# You are given a long string. Return the top k most common consecutive word pairs (bigrams). 
# Use itertools to generate the pairs.

from itertools import pairwise
from collections import Counter 

def finder(text_data, top_k):
    words = text_data.split()
    
    bigrams = pairwise(words)
    count = Counter(bigrams)
    return [biogram for biogram, _ in count.most_common(top_k)]

def main():
    text = "the cat sat on the mat the cat sat"
    top_k = 2
    print(finder(text, top_k))

if __name__ == '__main__':
    main()
